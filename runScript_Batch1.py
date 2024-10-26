# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:55:02 2019

@author: Wei
"""

from caiman_pipeline import caiman_process_session
from manifold_processing import runIsomapGrid, runLLEGrid

sessionDirsJZ207 = [
                    'E:\\Data\\Endoscope\\JZ207\\2018-08-16',
                    'E:\\Data\\Endoscope\\JZ207\\2018-08-17',
                    'E:\\Data\\Endoscope\\JZ207\\2018-08-23',
                    'E:\\Data\\Endoscope\\JZ207\\2018-08-27',
                    'E:\\Data\\Endoscope\\JZ207\\2018-08-28',
                    'E:\\Data\\Endoscope\\JZ207\\2018-08-29',
                    'E:\\Data\\Endoscope\\JZ207\\2018-08-30',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-10',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-11',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-12',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-14',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-16',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-18',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-20',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-24',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-26',
                    'E:\\Data\\Endoscope\\JZ207\\2018-09-27',
                    'E:\\Data\\Endoscope\\JZ207\\2018-11-03',
                    'E:\\Data\\Endoscope\\JZ207\\2018-11-04',
                    'E:\\Data\\Endoscope\\JZ207\\2018-11-27',
                    'E:\\Data\\Endoscope\\JZ207\\2018-11-28',
                    'E:\\Data\\Endoscope\\JZ207\\2018-11-29',
                    'E:\\Data\\Endoscope\\JZ207\\2018-11-30',
                    'E:\\Data\\Endoscope\\JZ207\\2018-12-06',
                    'E:\\Data\\Endoscope\\JZ207\\2018-12-09',
                    'E:\\Data\\Endoscope\\JZ207\\2018-12-11',
                    'E:\\Data\\Endoscope\\JZ207\\2018-12-12',
                    'E:\\Data\\Endoscope\\JZ207\\2018-12-14',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-17',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-19',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-21',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-23',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-26',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-28',
#                    'E:\\Data\\Endoscope\\JZ207\\2018-12-30',
#                    'E:\\Data\\Endoscope\\JZ207\\2019-01-02',
#                    'E:\\Data\\Endoscope\\JZ207\\JZ207_tee1',
                    ]

sessionDirsJZ209 = [
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-12',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-13',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-20',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-24',
#                    'E:\\Data\\Endoscope\\JZ209\\2018-09-27',
                    ]

sessionDirsJZ211 = [
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-07',
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-08',
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-09',
#                    'E:\\Data\\Endoscope\\JZ211\\2019-01-10',
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
                    ]

animalSessionList = [sessionDirsJZ207, sessionDirsJZ209, sessionDirsJZ211, 
                     sessionDirsJZ218, sessionDirsJZ219]


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


resultName = 'CaImAn_Results_V1'
for animalSession in animalSessionList:
    for sessionDir in animalSession:
        runIsomapGrid(sessionDir, resultName, 'Isomap_Cnorm_10Hz_Vmin10_Rmin100_2D_10_100_5.mat', 
                      n_components = 2, velRange = [10, 1000], trainBlockList = [], maxRespThr = 100,
                      dataType = 'C', timeScaleDown = 3, n_neighbors_list = range(10,105,5), normFlag = True)


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
