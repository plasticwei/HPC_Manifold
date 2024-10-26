# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:55:02 2019

@author: Wei
"""

from caiman_pipeline1a import caiman_process_session

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
#                    'E:\\Data\\Endoscope\\JZ207\\2019-02-14',
#                    'E:\\Data\\Endoscope\\JZ207\\2019-02-15',
#                    'E:\\Data\\Endoscope\\JZ207\\JZ207_tee1',
#                    'E:\\Data\\Endoscope\\JZ207\\JZ207_tee_circle_1',
#                    'E:\\Data\\Endoscope\\JZ207\\JZ207_tee_circle_2',
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
#                    'E:\\Data\\Endoscope\\JZ211\\2019-03-05',
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
#                    'E:\\Data\\Endoscope\\JZ218\\2019-02-25',
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
#                    'E:\\Data\\Endoscope\\JZ219\\2019-02-25',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-02-28',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-03-01',
#                    'E:\\Data\\Endoscope\\JZ219\\2019-03-04',
                    ]

sessionDirsJZ222 = [
#                    'E:\\Data\\Endoscope\\JZ222\\2019-02-25',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-04',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-05',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-06',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-07',
#                    'E:\\Data\\Endoscope\\JZ222\\2019-03-08',
                    ]


sessionDirsJZ224 = [
#                    'E:\\Data\\Endoscope\\JZ224\\2019-02-25',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-04',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-05',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-06',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-07',
#                    'E:\\Data\\Endoscope\\JZ224\\2019-03-08',
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

sessionDirsJZ231 = [
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-02',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-06-04',
                    'E:\\Data\\Endoscope\\JZ231\\2019-06-25',
                    'E:\\Data\\Endoscope\\JZ231\\2019-06-26',
                    ]


sessionDirsTemp = [
#                    'E:\\Data\\Endoscope\\Temp',
                    ]
sessionDirsWG037 = [
#                    'E:\\Data\\Endoscope\\WG037\\WG037S04',
                    ]

animalSessionList = [sessionDirsJZ207, sessionDirsJZ209, sessionDirsJZ211, 
                     sessionDirsJZ222, sessionDirsJZ224, sessionDirsJZ226,
                     sessionDirsJZ218, sessionDirsJZ219, sessionDirsTemp,
                     sessionDirsWG037, sessionDirsJZ231]


## IMPORTANT!! Copy and paste to Ipython
 
resultName = 'CaImAn_Results_V1a'

for animalSession in animalSessionList:
    for sessionDir in animalSession:
        caiman_process_session(sessionDir, resultName)


