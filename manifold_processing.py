# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:22:54 2019

@author: Wei
"""

import os
import numpy as np
import scipy.io as sio
from sklearn import manifold, decomposition
from time import time
import umap
from bonsai_funcs import loadBonsaiDataSession, getVideoList

def loadData(sessionDir, resultName, timeScaleDown, trainBlockList, maxRespThr,
             velRange, dataType, normFlag, exCellList):
    # Load the timestamps and tracking data of each block in the session
    [tsList, locList, velList] = loadBonsaiDataSession(sessionDir)
    videoList = getVideoList(sessionDir)
    
    # Load CaImAn processing results
    resultDir = os.path.join(sessionDir,resultName)
    fileList = [os.path.join(resultDir,f) for f in os.listdir(resultDir)
        if f.endswith('.npz')]
    resultFile = fileList[0]
    resultData = np.load(resultFile)
    
    # Parse CaImAn processing results
    C = resultData['C']
    YrA = resultData['YrA']
    S = resultData['S']
    idx_components = resultData['idx_components']
    
    if 'V' in resultData:
        V = resultData['V']

    # Get the range of indices of each block    
    if 'rangeList' in resultData:
        rangeList = resultData['rangeList']
    else:
        rangeList = []
        for thisList in videoList:
            thisListSize = np.shape(thisList)[0]
            rangeList.extend([range(1000, (thisListSize-1)*1000)])
            
    # Stitch Bonsai data selected by rangeList from each block into one chunk
    timestamps = []
    location = []
    velocity = []
    sampleFlags = []
    for i in range(len(rangeList)):
        if (i > 0):
            thisTS = tsList[i][rangeList[i]]
            thisTS = thisTS - thisTS[0]
            thisTS = thisTS + timestamps[-1]
            timestamps.extend(thisTS)
        else:
            timestamps.extend(tsList[i][rangeList[i]])
        location.extend(locList[i][rangeList[i]])
        velocity.extend(velList[i][rangeList[i]])
        if len(trainBlockList) > 0:
            if (i+1) in trainBlockList:
                sampleFlags.extend(np.ones(len(rangeList[i])))
            else:
                sampleFlags.extend(np.zeros(len(rangeList[i])))
        else:
            sampleFlags.extend(np.ones(len(rangeList[i])))    

    # Make sure the CaImAn results match the Bonsai data
    if len(timestamps) != np.shape(C)[1]:
        print('Data size mismatch!')

    # Eliminate cells wil low responses
    idxResp = np.where(np.max(C, axis=1) > maxRespThr)
    
    good_cell_idx = np.intersect1d(idx_components, idxResp)
    train_cell_idx = np.setdiff1d(good_cell_idx, exCellList)

    # Select data type for processing
    if dataType == 'C':
        neuroData = C[train_cell_idx,:]
    elif dataType == 'Craw':
        neuroData = C[train_cell_idx,:] + YrA[train_cell_idx,:]
    elif dataType == 'S':
        neuroData = S[train_cell_idx,:]
    elif dataType == 'V':
        neuroData = V
    else:
        print('Incorrect data type!')

    # Downsample the data    
    timeIdx = range(0, np.shape(C)[1], timeScaleDown)
    X = np.transpose(neuroData[:, timeIdx])
    Cout = np.transpose(C[:, timeIdx])
    thisTimestamps = np.asarray(timestamps)[timeIdx]
    thisVel = np.asarray(velocity)[timeIdx]
    thisLoc = np.asarray(location)[timeIdx,:]
    thisSampleFlags = np.asarray(sampleFlags)[timeIdx]
    
    # Select the training samples according to velocity
    velIdx = np.intersect1d(np.where(np.asarray(thisVel) > velRange[0]), 
                            np.where(np.asarray(thisVel) <= velRange[1]))
    
    # Select training samples from designiated data blocks
    trainBlockIdx = np.where(np.asarray(thisSampleFlags) > 0)
    
    # Combine the two
    trainIdx = np.intersect1d(velIdx, trainBlockIdx)

    # Normalizing data if normFlag is true
    if normFlag:
        X_norm = X.copy()
        for i in range(np.shape(X_norm)[1]):
            X_norm[:,i] = X_norm[:,i] - np.min(X[:,i])
            X_norm[:,i] = X_norm[:,i] / np.max(X[:,i])
        X = X_norm
    
        
    # Set the cells used to train manifold
    X_train = X[trainIdx, :]
        
    #Return the loaded data
    return Cout, X, X_train, trainIdx, thisTimestamps, thisVel, thisLoc, rangeList, good_cell_idx, train_cell_idx


def runIsomapGrid(sessionDir, resultName, outputName, 
                  n_components = 2, n_neighbors_list = [10], trainBlockList = [], maxRespThr = 50,
                  timeScaleDown = 3, velRange = [0,1000], dataType = 'C', normFlag = False, exCellList = []):
    # Load data from Bonsai runs and CaImAn processing
    Cout, X, X_train, trainIdx, thisTimestamps, thisVel,\
    thisLoc, rangeList, good_cell_idx, train_cell_idx = loadData(sessionDir = sessionDir,
                                                 resultName = resultName,
                                                 timeScaleDown = timeScaleDown,
                                                 trainBlockList = trainBlockList,
                                                 maxRespThr = maxRespThr,
                                                 velRange = velRange,
                                                 dataType = dataType,
                                                 normFlag = normFlag,
                                                 exCellList = exCellList)
    resultDir = os.path.join(sessionDir,resultName)
    
    # Run isomap algorithm 
    all_Y = []
    all_Error = []
    for n_neighbors in n_neighbors_list:
        print("")
        print("Isomap %d dims, %d neighbors" % (n_components, n_neighbors))
        t0 = time()
        IsoModel = manifold.Isomap(n_neighbors, n_components, n_jobs=-1).fit(X_train)
        Y = IsoModel.transform(X)
        t1 = time()
        all_Y.extend([Y])
        all_Error.extend([IsoModel.reconstruction_error()])
        print("Time elapsed: %.2g sec" % (t1 - t0))
        print("Reconstruction error: %.2f" % IsoModel.reconstruction_error())

    # Saving output data
    outdata = dict()
    outdata['C'] = Cout
    outdata['X'] = X
    outdata['X_train'] = X_train
    outdata['trainIdx'] = trainIdx
    outdata['all_Y'] = all_Y
    outdata['all_Error'] = all_Error
    outdata['timestamps'] = thisTimestamps
    outdata['velocity'] = thisVel
    outdata['location'] = thisLoc
    outdata['n_neighbors_list'] = n_neighbors_list
    outdata['n_components'] = n_components
    outdata['timeScaleDown'] = timeScaleDown
    outdata['velRange'] = velRange
    outdata['dataType'] = dataType
    outdata['normFlag'] = normFlag
    outdata['rangeList'] = rangeList
    outdata['good_cell_idx'] = good_cell_idx
    outdata['train_cell_idx'] = train_cell_idx

    outputFile = os.path.join(resultDir, outputName)
    print("Saving " + outputFile)
    print("\n")
    
    sio.savemat(outputFile, outdata)
        
    
def runLLEGrid(sessionDir, resultName, outputName, trainBlockList = [], maxRespThr = 50,
                  n_components = 2, n_neighbors_list = [10], LLEmethod = 'modified', 
                  eigen_solver = 'auto', timeScaleDown = 3,  velRange = [0, 1000], 
                  dataType = 'C', normFlag = False):
    
    # Load data from Bonsai runs and CaImAn processing
    Cout, X, X_train, trainIdx, thisTimestamps, thisVel,\
    thisLoc, rangeList, good_cell_idx = loadData(sessionDir = sessionDir,
                                                 resultName = resultName,
                                                 timeScaleDown = timeScaleDown,
                                                 trainBlockList = trainBlockList,
                                                 maxRespThr = maxRespThr,
                                                 velRange = velRange,
                                                 dataType = dataType,
                                                 normFlag = normFlag)
    resultDir = os.path.join(sessionDir,resultName)
   
    
    # Run LLE algorithm 
    all_Y = []
    all_Error = []
    for n_neighbors in n_neighbors_list:
        print("")
        print("LLE %d dims, %d neighbors" % (n_components, n_neighbors))
        t0 = time()
        LLEModel = manifold.LocallyLinearEmbedding(n_neighbors, n_components,
                                            eigen_solver='dense',
                                            method=LLEmethod).fit(X_train)
        Y = LLEModel.transform(X)
        t1 = time()
        all_Y.extend([Y])
        all_Error.extend([LLEModel.reconstruction_error_])
        print("Time elapsed: %.2g sec" % (t1 - t0))
        print("Reconstruction error: %.2f" % LLEModel.reconstruction_error_)

    # Saving output data
    outdata = dict()
    outdata['C'] = Cout
    outdata['X'] = X
    outdata['X_train'] = X_train
    outdata['trainIdx'] = trainIdx
    outdata['all_Y'] = all_Y
    outdata['all_Error'] = all_Error
    outdata['timestamps'] = thisTimestamps
    outdata['velocity'] = thisVel
    outdata['location'] = thisLoc
    outdata['n_neighbors_list'] = n_neighbors_list
    outdata['n_components'] = n_components
    outdata['timeScaleDown'] = timeScaleDown
    outdata['velRange'] = velRange
    outdata['dataType'] = dataType
    outdata['normFlag'] = normFlag
    outdata['rangeList'] = rangeList
    outdata['good_cell_idx'] = good_cell_idx

    outputFile = os.path.join(resultDir, outputName)
    print("Saving " + outputFile)
    print("\n")
    
    sio.savemat(outputFile, outdata)
        
def runUmapGrid(sessionDir, resultName, outputName, min_dist = 0.2, random_state = 42,
                  n_components = 2, n_neighbors_list = [10], trainBlockList = [], maxRespThr = 50,
                  timeScaleDown = 3, velRange = [0,1000], dataType = 'C', normFlag = False):
    # Load data from Bonsai runs and CaImAn processing
    Cout, X, X_train, trainIdx, thisTimestamps, thisVel,\
    thisLoc, rangeList, good_cell_idx = loadData(sessionDir = sessionDir,
                                                 resultName = resultName,
                                                 timeScaleDown = timeScaleDown,
                                                 trainBlockList = trainBlockList,
                                                 maxRespThr = maxRespThr,
                                                 velRange = velRange,
                                                 dataType = dataType,
                                                 normFlag = normFlag)
    resultDir = os.path.join(sessionDir,resultName)
    
    # Run isomap algorithm 
    all_Y = []
    all_Error = []
    for n_neighbors in n_neighbors_list:
        print("")
        print("Umap %d dims, %d neighbors" % (n_components, n_neighbors))
        t0 = time()
        UModel = umap.UMAP(random_state=42,
                    n_neighbors=n_neighbors,
                    min_dist=min_dist,
                    n_components=n_components)

        UModel.fit(X_train)
        Y = UModel.transform(X)
        t1 = time()
        all_Y.extend([Y])
        all_Error.extend([])
        print("Time elapsed: %.2g sec" % (t1 - t0))
#        print("Reconstruction error: %.2f" % IsoModel.reconstruction_error())

    # Saving output data
    outdata = dict()
    outdata['C'] = Cout
    outdata['X'] = X
    outdata['X_train'] = X_train
    outdata['trainIdx'] = trainIdx
    outdata['all_Y'] = all_Y
    outdata['all_Error'] = all_Error
    outdata['timestamps'] = thisTimestamps
    outdata['velocity'] = thisVel
    outdata['location'] = thisLoc
    outdata['n_neighbors_list'] = n_neighbors_list
    outdata['n_components'] = n_components
    outdata['timeScaleDown'] = timeScaleDown
    outdata['velRange'] = velRange
    outdata['dataType'] = dataType
    outdata['normFlag'] = normFlag
    outdata['rangeList'] = rangeList
    outdata['good_cell_idx'] = good_cell_idx

    outputFile = os.path.join(resultDir, outputName)
    print("Saving " + outputFile)
    print("\n")
    
    sio.savemat(outputFile, outdata)
        
    
    
    
    
    
    
    
    
    
    
    
    
    