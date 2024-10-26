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
#                    [3],
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
#                    [2],
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
#                    [2],
#                    [2],
#                    [2],
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
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-24',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-26',
#                    'E:\\Data\\Endoscope\\JZ231\\2019-07-27',
#                    'E:\\Data\\Endoscope\\JZ231\\JZ231S01',
                    ]
sessionBlksJZ231 = [
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [1,2],
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
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
                    ]

sessionDirsWG027 = [
#                    'E:\\Data\\Endoscope\\WG027\\WG027S03',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S04',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S05',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S06',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S07',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S08',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S09',
                    ]
sessionBlksWG027 = [
#                    [3],
#                    [3],
#                    [3],
#                    [2],
#                    [2],
#                    [1],
#                    [1],
                    ]

sessionDirsWG032 = [
#                    'E:\\Data\\Endoscope\\WG032\\WG032S03',
#                    'E:\\Data\\Endoscope\\WG032\\WG032S04',
#                    'E:\\Data\\Endoscope\\WG032\\WG032S05',
#                    'E:\\Data\\Endoscope\\WG032\\WG032S06',
#                    'E:\\Data\\Endoscope\\WG032\\WG032S07',
#                    'E:\\Data\\Endoscope\\WG032\\WG032S08',
#                    'E:\\Data\\Endoscope\\WG032\\WG032S09',
                    ]
sessionBlksWG032 = [
#                    [3],
#                    [2],
#                    [2],
#                    [3],
#                    [2],
#                    [1],
#                    [1],
                    ]

sessionDirsWG034 = [
#                    'E:\\Data\\Endoscope\\WG034\\WG034S03',
#                    'E:\\Data\\Endoscope\\WG034\\WG034S04',
#                    'E:\\Data\\Endoscope\\WG034\\WG034S05',
#                    'E:\\Data\\Endoscope\\WG034\\WG034S06',
#                    'E:\\Data\\Endoscope\\WG034\\WG034S07',
#                    'E:\\Data\\Endoscope\\WG034\\WG034S08',
#                    'E:\\Data\\Endoscope\\WG034\\WG034S09',
                    ]
sessionBlksWG034 = [
#                    [3],
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [1],
#                    [1],
                    ]

sessionDirsWG035 = [
#                    'E:\\Data\\Endoscope\\WG035\\WG035S03',
#                    'E:\\Data\\Endoscope\\WG035\\WG035S04',
#                    'E:\\Data\\Endoscope\\WG035\\WG035S05',
#                    'E:\\Data\\Endoscope\\WG035\\WG035S06',
#                    'E:\\Data\\Endoscope\\WG035\\WG035S07',
#                    'E:\\Data\\Endoscope\\WG035\\WG035S08',
#                    'E:\\Data\\Endoscope\\WG035\\WG035S09',
                    ]
sessionBlksWG035 = [ 
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [1],
#                    [1],
                    ]

sessionDirsWG036 = [
#                    'E:\\Data\\Endoscope\\WG036\\WG036S04',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S05',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S06',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S07',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S08',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S09',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S10',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S11',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S12',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S13',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S14',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S15',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S16',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S17',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S18',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S19',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S20',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S21',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S22',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S23',
#                    'E:\\Data\\Endoscope\\WG036\\WG036S24',
                    ]
sessionBlksWG036 = [ 
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
#                    [1],
#                    [1],
                    ]

sessionDirsWG037 = [
#                    'E:\\Data\\Endoscope\\WG037\\WG037S04',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S05',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S06',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S07',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S08',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S09',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S10',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S11',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S12',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S13',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S14',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S15',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S16',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S17',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S18',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S19',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S20',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S21',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S22',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S23',
#                    'E:\\Data\\Endoscope\\WG037\\WG037S24',
                    ]
sessionBlksWG037 = [ 
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
#                    [1],
#                    [1],
                    ]

sessionDirsQX077 = [
#                    'E:\\Data\\Endoscope\\QX077\\QX077S01',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S02',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S03',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S04',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S05',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S06',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S07',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S08',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S09',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S10',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S11',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S12',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S13',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S14',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S15',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S16',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S17',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S18',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S19',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S20',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S21',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S22',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S23',
#                    'E:\\Data\\Endoscope\\QX077\\QX077S24',
                    'E:\\Data\\Endoscope\\QX077\\QX077S25',
                    'E:\\Data\\Endoscope\\QX077\\QX077S26',
                    'E:\\Data\\Endoscope\\QX077\\QX077S27',
                    'E:\\Data\\Endoscope\\QX077\\QX077S28',
                    ]

sessionBlksQX077 = [ 
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
#                    [1],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
                    [1],
                    [1],
                    [1],
                    [1],
                    ]

sessionDirsQX078 = [
#                    'E:\\Data\\Endoscope\\QX078\\QX078S01',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S02',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S03',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S04',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S05',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S06',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S07',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S08',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S09',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S10',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S11',
#                    'E:\\Data\\Endoscope\\QX078\\QX078S12',
                    ]

sessionBlksQX078 = [ 
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
                    ]

sessionDirsJZ236 = [
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S01',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S02',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S03',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S04',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S05',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S06',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S07',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S08',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S09',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S10',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S11',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S12',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S13',
#                    'E:\\Data\\Endoscope\\JZ236\\JZ236S14',
                    ]

sessionBlksJZ236 = [ 
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
                    ]

sessionDirsTH42891 = [
#                    'E:\Data\Endoscope\TH42891\TH42891SXD1',
#                    'E:\Data\Endoscope\TH42891\TH42891SXD2',
#                    'E:\Data\Endoscope\TH42891\TH42891SXD3',
                    'E:\Data\Endoscope\TH42891\TH42891SXD4',
                    ]

sessionBlksTH42891 = [ 
                    [2],
                    [2],
                    [2],
                    [2],
                    ]

animalSessionList = [sessionDirsJZ207, sessionDirsJZ209, sessionDirsJZ211, 
                     sessionDirsJZ218, sessionDirsJZ219, sessionDirsJZ222,
                     sessionDirsJZ224, sessionDirsJZ226, sessionDirsJZ229,
                     sessionDirsJZ231, sessionDirsWG027, sessionDirsWG032,
                     sessionDirsWG035, sessionDirsWG034, sessionDirsWG036,
                     sessionDirsWG037, sessionDirsQX077, sessionDirsQX078,
                     sessionDirsJZ236, sessionDirsTH42891]

sessionBlksList = [sessionBlksJZ207, sessionBlksJZ209, sessionBlksJZ211, 
                     sessionBlksJZ218, sessionBlksJZ219, sessionBlksJZ222,
                     sessionBlksJZ224, sessionBlksJZ226, sessionBlksJZ229,
                     sessionBlksJZ231, sessionBlksWG027, sessionBlksWG032,
                     sessionBlksWG035, sessionBlksWG034, sessionBlksWG036,
                     sessionBlksWG037, sessionBlksQX077, sessionBlksQX078,
                     sessionBlksJZ236, sessionBlksTH42891]

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
processID = 'Isomap_Cnorm_10Hz_Vmin0_Blks2_Rmin100_2D_10_100_5'
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
#processID = 'Isomap_Cnorm_10Hz_Vmin0_Blks1_Rmin100_3D_105_150_5'
#for animalSession, sessionBlks in zip(animalSessionList, sessionBlksList):
#    for sessionDir, sessionBlk  in zip(animalSession, sessionBlks):
#        sess_strs = sessionDir.split('\\')
#        tempFileName = tempFolder + '\\' + sess_strs[3] + '_'+sess_strs[4]\
#                        + '_' + resultName + '_' + processID + '.tmp'
#        if not os.path.isfile(tempFileName):
#            f = open(tempFileName, "w")
#            runIsomapGrid(sessionDir, resultName, processID+'.mat', 
#                          n_components = 3, velRange = [0, 1000], trainBlockList = sessionBlk, \
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

