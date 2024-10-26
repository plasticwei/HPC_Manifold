# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:55:02 2019

@author: Wei
"""

from caiman_pipeline1 import caiman_process_session
from manifold_processing import runIsomapGrid, runLLEGrid, runUmapGrid
import os.path

tempFolder = 'F:\\Caiman_Workfolder\\Temp'

sessionDirsJZ207 = [
#                    'E:\\Data\\Endoscope\\JZ207\\2018-08-16',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-08-17',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-08-23',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-08-27',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-08-28',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-08-29',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-08-30',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-10',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-11',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-12',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-14',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-16',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-18',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-20',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-24',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-26',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-09-27',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-11-03',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-11-04',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-11-27',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-11-28',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-11-29',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-11-30',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-06',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-09',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-11',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-12',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-14',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-17',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-19',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-21',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-23',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-26',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-28',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-30',
#                    'E:\\Data\\Endoscope\\JZ207\\2019-01-02',
#                    'E:\\Data\\Endoscope\\JZ207\\JZ207_tee1',
#                    'E:\\Data\\Endoscope\\JZ207\\JZ207_tee_circle_1',
#                    'E:\\Data\\Endoscope\\JZ207\\JZ207_tee_circle_2',
#                    'E:\\Data\\Endoscope\\JZ207\\2019-04-25',
                    ]
sessionBlksJZ207 = [
#                    [1,2],
                    ]


sessionDirsJZ209 = [
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-12',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-13',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-20',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-24',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-27',
                    ]
sessionBlksJZ209 = [
                    ]

sessionDirsJZ211 = [
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-07',
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-08',
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-09',
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-10',
                    ]
sessionBlksJZ211 = [
                    ]

sessionDirsJZ218 = [
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-14',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-15',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-18',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-20',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-21',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-22',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-23',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-25',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-27',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-01-29',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-02-18',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-02-19',
#                    'E:\\Data\\Endoscope\\JZ218\\2019-02-25',
                    ]
sessionBlksJZ218 = [
                    ]

sessionDirsJZ219 = [
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-19',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-20',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-21',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-22',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-23',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-25',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-27',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-01-29',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-02-18',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-02-19',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-02-25',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-02-28',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-03-01',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-03-04',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-03-05',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-04-23',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-05-13',
                     ]
sessionBlksJZ219 = [
#                    [1],
#                    [1],
#                    [1,2],
#                    [1,2],
#                    [1,2,3],
#                    [1],
#                    [1],
                    ]

sessionDirsJZ222 = [
#                    'E:\\Data\\Endoscope\\JZ222\\2019-02-25',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-01',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-04',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-05',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-06',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-07',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-08',
                    ]
sessionBlksJZ222 = [
#                    [1],
#                    [1,2],
#                    [1,2],
#                    [1],
#                    [1]
                    ]


sessionDirsJZ224 = [
#                    'E:\\Data\\Endoscope\\JZ224\\2019-02-25',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-01',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-04',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-05',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-06',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-07',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-08',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-04-22',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-05-08',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-05-14',
                    ]

sessionBlksJZ224 = [
#                    [1],
#                    [1],
#                    [1,2],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
                    ]

sessionDirsJZ226 = [
#                    'E:\\Data\\Endoscope\\JZ226\\2019-02-28',
#                    'E:\\Data\\Endoscope\\JZ226\\2019-03-01',
#                    'E:\\Data\\Endoscope\\JZ226\\2019-03-04',
#                    'E:\\Data\\Endoscope\\JZ226\\2019-03-05',
#                    'E:\\Data\\Endoscope\\JZ226\\2019-03-06',
#                    'E:\\Data\\Endoscope\\JZ226\\2019-03-07',
#                    'E:\\Data\\Endoscope\\JZ226\\2019-03-08',
                    ]
sessionBlksJZ226 = [
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1]
                    ]

sessionDirsJZ229 = [
#                    'E:\\Data\\Endoscope\\JZ229\\2019-03-22',
#                    'E:\\Data\\Endoscope\\JZ229\\2019-03-24',
#                    'E:\\Data\\Endoscope\\JZ229\\2019-03-26',
#                    'E:\\Data\\Endoscope\\JZ229\\2019-03-28',
#                    'E:\\Data\\Endoscope\\JZ229\\2019-03-31',
#                    'E:\\Data\\Endoscope\\JZ229\\2019-04-04',
                    ]
sessionBlksJZ229 = [
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1,2],
#                    [1]
                    ]
sessionDirsJZ231 = [
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-02',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-03',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-06',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-07',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-15',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-17',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-24',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-25',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-27',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-28',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-29',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-30',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-05-31',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-01',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-02',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-04',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-05',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-06',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-07',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-08',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-10',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-11',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-12',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-13',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-14',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-15',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-17',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-18',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-19',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-20',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-21',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-24',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-25',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-26',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-27',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-28',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-29',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-01',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-02',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-03',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-05',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-08',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-19',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-23',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-24',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-26',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-27',
                    ]
sessionBlksJZ231 = [
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1,2],
#                    [1,2],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1,2],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1,2],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
                    ]

animalSessionList = [sessionDirsJZ207, sessionDirsJZ209, sessionDirsJZ211, 
                     sessionDirsJZ218, sessionDirsJZ219, sessionDirsJZ222,
                     sessionDirsJZ224, sessionDirsJZ226, sessionDirsJZ229,
                     sessionDirsJZ231]

sessionBlksList = [sessionBlksJZ207, sessionBlksJZ209, sessionBlksJZ211, 
                     sessionBlksJZ218, sessionBlksJZ219, sessionBlksJZ222,
                     sessionBlksJZ224, sessionBlksJZ226, sessionBlksJZ229,
                     sessionBlksJZ231]


## IMPORTANT!! Copy and paste to Ipython

#resultName = 'CaImAn_Results_V1'
#for animalSession in animalSessionList:
#    for sessionDir in animalSession:
#        caiman_process_session(sessionDir, resultName)
#


#resultName = 'CaImAn_Results_V1'
#for animalSession in animalSessionList:
#    for sessionDir in animalSession:
#        runIsomapGrid(sessionDir, resultName, 'Isomap_C_10Hz_Vmin0_Rmin100_2D_10_60_5.mat', 
#                      n_components = 2, velRange = [0, 1000], trainBlockList = [], maxRespThr = 100,
#                      dataType = 'C', timeScaleDown = 3, n_neighbors_list = range(10,65,5))


#resultName = 'CaImAn_Results_V1'
#processID = 'Isomap_Cnorm_10Hz_Vmin0_Blks_Rmin50_2D_10_100_5'
#for animalSession in animalSessionList:
#    for sessionDir in animalSession:
#        sess_strs = sessionDir.split('\\')
#        tempFileName = tempFolder + '\\' + sess_strs[3] + '_'+sess_strs[4]\
#                        + '_' + resultName + '_' + processID + '.tmp'
#        if not os.path.isfile(tempFileName):
#            f = open(tempFileName, "w")
#            runIsomapGrid(sessionDir, resultName, processID+'.mat', 
#                          n_components = 2, velRange = [0, 1000], trainBlockList = [], \
#                          maxRespThr = 50, dataType = 'C', timeScaleDown = 3, \
#                          n_neighbors_list = range(10,105,5), normFlag = True)
#            f.close()
# 


resultName = 'CaImAn_Results_V1'
processID = 'Isomap_Cnorm_10Hz_Vmin0_Blks1_Rmin100_2D_10_100_5'
for animalSession, sessionBlks in zip(animalSessionList, sessionBlksList):
    for sessionDir, sessionBlk  in zip(animalSession, sessionBlks):
        sess_strs = sessionDir.split('\\')
        tempFileName = tempFolder + '\\' + sess_strs[3] + '_'+sess_strs[4]\
                        + '_' + resultName + '_' + processID + '.tmp'
        if not os.path.isfile(tempFileName):
            f = open(tempFileName, "w")
            runIsomapGrid(sessionDir, resultName, processID+'.mat', 
                          n_components = 2, velRange = [0, 1000], trainBlockList = sessionBlk, \
                          maxRespThr = 100, dataType = 'C', timeScaleDown = 3, \
                          n_neighbors_list = range(10,105,5), normFlag = True)
            f.close()
 
#
#resultName = 'CaImAn_Results_V1'
#processID = 'Isomap_Cnorm_10Hz_Vmin0_Blks1_Rmin100_2D_105_150_5'
#for animalSession, sessionBlks in zip(animalSessionList, sessionBlksList):
#    for sessionDir, sessionBlk  in zip(animalSession, sessionBlks):
#        sess_strs = sessionDir.split('\\')
#        tempFileName = tempFolder + '\\' + sess_strs[3] + '_'+sess_strs[4]\
#                        + '_' + resultName + '_' + processID + '.tmp'
#        if not os.path.isfile(tempFileName):
#            f = open(tempFileName, "w")
#            runIsomapGrid(sessionDir, resultName, processID+'.mat', 
#                          n_components = 2, velRange = [0, 1000], trainBlockList = sessionBlk, \
#                          maxRespThr = 100, dataType = 'C', timeScaleDown = 3, \
#                          n_neighbors_list = range(105,155,5), normFlag = True)
#            f.close()


#resultName = 'CaImAn_Results_V1'
#processID = 'Umap_Cnorm_10Hz_Vmin0_Blks_Rmin100_2D_Dist005_10_100_5'
#for animalSession, sessionBlks in zip(animalSessionList, sessionBlksList):
#    for sessionDir, sessionBlk  in zip(animalSession, sessionBlks):
#        sess_strs = sessionDir.split('\\')
#        tempFileName = tempFolder + '\\' + sess_strs[3] + '_'+sess_strs[4]\
#                        + '_' + resultName + '_' + processID + '.tmp'
#        print(tempFileName)
#        if not os.path.isfile(tempFileName):
#            f = open(tempFileName, "w")
#            runUmapGrid(sessionDir, resultName, processID+'.mat', min_dist = 0.05, \
#                          n_components = 2, velRange = [0, 1000], trainBlockList = sessionBlk, \
#                          maxRespThr = 100, dataType = 'C', timeScaleDown = 3, \
#                          n_neighbors_list = range(10,105,5), normFlag = True)
#            f.close()
 

#resultName = 'CaImAn_Results_V1'
#for animalSession in animalSessionList:
#    for sessionDir in animalSession:
#        runLLEGrid(sessionDir, resultName, 'LLE_Cnorm_10Hz_Vmin0_Rmin100_2D_10_60_5.mat', trainBlockList = [],
#                      n_components = 2, velRange = [0, 1000], eigen_solver='auto', maxRespThr = 100,
#                      dataType = 'C', timeScaleDown = 3, n_neighbors_list = range(10,65,5), normFlag = True)


#resultName = 'CaImAn_Results_V1'
#for animalSession in animalSessionList:
#    for sessionDir in animalSession:
#        runIsomapGrid(sessionDir, resultName, 'Isomap_Cnorm_10Hz_Vmin0_Rmin100_3D_10_60_5.mat', 
#                      n_components = 3, velRange = [0, 1000], trainBlockList = [], maxRespThr = 100,
#                      dataType = 'C', timeScaleDown = 3, n_neighbors_list = range(10,65,5), normFlag = True)

