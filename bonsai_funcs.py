# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:41:05 2019

@author: Wei
"""

import csv
import os
import datetime
import numpy as np
from scipy import signal


def loadTimestamp(csvFileName):
    # Read timestamps in date time format.
    # The data should be the first column of the csv file.
    rawTimestamps = []
    with open(csvFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        line_count = 0
        for row in csv_reader:
            rawTimestamps.append(datetime.datetime.strptime(row[0][0:26],'%Y-%m-%dT%H:%M:%S.%f'))
            line_count += 1
        print(f'Processed {line_count} lines.')

    return rawTimestamps

def load2DLocation(csvFileName):
    # Load tracking data.
    # The data should be the second and third columns of the csv file.
    loc2D = []
    with open(csvFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        line_count = 0
        for row in csv_reader:
            loc2D.append((float(row[1]),float(row[2])))
            line_count += 1
    loc2D = np.asarray(loc2D)
        
    # Fixing bad data points due to tracking errors
    for i in range(np.shape(loc2D)[0]):
        if np.isnan(loc2D[i,0]) or (loc2D[i,0] < 0.01):
            loc2D[i,0] = loc2D[i-1,0]
        if np.isnan(loc2D[i,1]) or (loc2D[i,1] < 0.01):
            loc2D[i,1] = loc2D[i-1,1]
            
    return loc2D

def calcVelocity(loc2D, timestampsTrack):
    # Calculate velocity from the 2D tracking data

    # Smoothing the location data
    b, a = signal.butter(3, 0.01)
    loc_smooth = signal.filtfilt(b, a, loc2D, axis = 0)
    
    # Calculating velocity
    velocity = np.zeros(np.shape(timestampsTrack))
    winSize = 50
    for i in range(np.shape(loc_smooth)[0]):
        if (i <= winSize) or (i >= np.shape(timestampsTrack)[0] - winSize):
            velocity[i] = 0
        else:
            dist = ((loc_smooth[i-winSize,0] -loc_smooth[i+winSize,0])**2 + 
                    (loc_smooth[i-winSize,1] -loc_smooth[i+winSize,1])**2)**0.5
            velocity[i] = dist / (timestampsTrack[i+winSize] - timestampsTrack[i-winSize])
    return velocity


def loadCSVData(csvFileEndo, csvFileTrack):
    # Loading the timestamps for 1p recordings and location tracking
    # Align the location data temporally with the 1p frames
    # Calculate the velocity from the tracking data
    # The output would be the timestamps of each 1p frame, and the associated
    # animal location and instantaneous velocity.
    
    # Load raw timestamps
    rawTimestampsEndo = loadTimestamp(csvFileEndo)
    rawTimestampsTrack = loadTimestamp(csvFileTrack)

    # Reference all timestamps w.r.t. to the first frame of the endoscope data
    zeroRef = lambda x:x-rawTimestampsEndo[0]
    timestampsEndo = np.asarray(list(map(datetime.timedelta.total_seconds, 
                                        list(map(zeroRef, rawTimestampsEndo)))))
    timestampsTrack = np.asarray(list(map(datetime.timedelta.total_seconds, 
                                        list(map(zeroRef, rawTimestampsTrack)))))
    
    # Load 2D tracking results
    loc2D = load2DLocation(csvFileTrack)
    
    # Calculate velocity based on tracking data
    velocity = calcVelocity(loc2D, timestampsTrack)

    # Find location and velocity of the animal at each time stamp of the endoscope data
    velTimeAligned = np.zeros(np.shape(timestampsEndo))
    loc2DTimeAligned = np.zeros((np.shape(timestampsEndo)[0],2))
    
    for i in range(np.shape(timestampsEndo)[0]):
        idx = np.argmin(np.abs(timestampsTrack - timestampsEndo[i]))
        velTimeAligned[i] = velocity[idx]
        loc2DTimeAligned[i] = loc2D[idx,:]

    return timestampsEndo, loc2DTimeAligned, velTimeAligned
    

def loadBonsaiDataDir(bonsaiDir):
    # Load csv data from a Bonsai recording folder
    
    fileListTrack = [os.path.join(bonsaiDir,f) for f in os.listdir(bonsaiDir)
        if f.endswith('.csv') and (f.find('pos-speed') >= 0)]
    csvFileTrack = fileListTrack[0]
    print(csvFileTrack)
    fileListEndo = [os.path.join(bonsaiDir,f) for f in os.listdir(bonsaiDir)
        if f.endswith('.csv') and (f.find('scope-vid-time') >= 0)]
    csvFileEndo = fileListEndo[0]
    print(csvFileEndo)
    
    [timestampsEndo, loc2DTimeAligned, velTimeAligned] = loadCSVData(csvFileEndo, csvFileTrack)
    return timestampsEndo, loc2DTimeAligned, velTimeAligned


def loadBonsaiDataSession(sessionDir):
    # Load csv data from a Bonsai recording session ordered by blocks
    blockDirList = [os.path.join(sessionDir,f) for f in os.listdir(sessionDir)
        if (f.find('block_') >= 0)]
    
    timestampsEndoList = []
    loc2DTimeAlignedList = []
    velTimeAlignedList = []
    
    for bonsaiDir in blockDirList:
        [timestampsEndo, loc2DTimeAligned, velTimeAligned] = loadBonsaiDataDir(bonsaiDir)
        timestampsEndoList.extend([timestampsEndo])
        loc2DTimeAlignedList.extend([loc2DTimeAligned])
        velTimeAlignedList.extend([velTimeAligned])
  
    return timestampsEndoList, loc2DTimeAlignedList, velTimeAlignedList
    

def getVideoList(sessionDir, fullPathFlag = False):
    # Get the list of raw scape videos from a Bonsai recording session ordered by blocks
    
    blockDirList = [os.path.join(sessionDir,f) for f in os.listdir(sessionDir)
        if (f.find('block_') >= 0)]
    
    videoList = []    
    for blockDir in blockDirList:
        if fullPathFlag:
            thisDirFiles = [os.path.join(blockDir,f) for f in os.listdir(blockDir)
                if f.endswith('.avi') and (f.find('rawscope') >= 0)]
        else:
            thisDirFiles = [os.path.join('',f) for f in os.listdir(blockDir)
                if f.endswith('.avi') and (f.find('rawscope') >= 0)]
        videoList.extend([thisDirFiles])
  
    return videoList
  









