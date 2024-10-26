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
                    ]

sessionDirsWG027 = [
#                    'E:\\Data\\Endoscope\\WG027\\WG027S03',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S04',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S05',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S06',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S07',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S08',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S09',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S10',
#                    'E:\\Data\\Endoscope\\WG027\\WG027S11',
                    ]
sessionBlksWG027 = [
#                    [3],
#                    [3],
#                    [3],
#                    [2],
#                    [2],
#                    [1],
#                    [1],
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
#                    'E:\\Data\\Endoscope\\WG032\\WG032S10',
#                    'E:\\Data\\Endoscope\\WG032\\WG032S11',
                    ]
sessionBlksWG032 = [
#                    [3],
#                    [2],
#                    [2],
#                    [3],
#                    [2],
#                    [1],
#                    [1],
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
#                    'E:\\Data\\Endoscope\\WG034\\WG034S10',
#                    'E:\\Data\\Endoscope\\WG034\\WG034S11',
                    ]
sessionBlksWG034 = [
#                    [3],
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [1],
#                    [1],
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
#                    'E:\\Data\\Endoscope\\WG035\\WG035S10',
#                    'E:\\Data\\Endoscope\\WG035\\WG035S11',
                    ]
sessionBlksWG035 = [ 
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [2],
#                    [1],
#                    [1],
#                    [1],
#                    [1],
                    ]

sessionDirsWG028 = [
#                    'E:\\Data\\Endoscope\\WG028\\WG028S03',
                    ]
sessionBlksWG028 = [ 
#                    [1],
                    ]

sessionDirsWG029 = [
#                    'E:\\Data\\Endoscope\\WG029\\WG029S03',
                    ]
sessionBlksWG029 = [ 
#                    [1],
                    ]

sessionDirsWG031 = [
#                    'E:\\Data\\Endoscope\\WG031\\WG031S02',
                    ]
sessionBlksWG031 = [ 
#                    [1],
                    ]

sessionDirsWG3037 = [
#                    'E:\\Data\\Endoscope\\WG3037\\WG3037S01',
#                    'E:\\Data\\Endoscope\\WG3037\\WG3037S02',
#                    'E:\\Data\\Endoscope\\WG3037\\WG3037S03',
#                    'E:\\Data\\Endoscope\\WG3037\\WG3037S04',
#                    'E:\\Data\\Endoscope\\WG3037\\WG3037S05',
#                    'E:\\Data\\Endoscope\\WG3037\\WG3037S06',
                    ]
sessionBlksWG3037 = [ 
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
                    ]

sessionDirsWG3038 = [
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S01',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S02',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S03',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S04',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S05',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S06',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S07',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S08',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S09',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S10',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S11',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S12',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S13',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S14',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S15',
#                    'E:\\Data\\Endoscope\\WG3038\\WG3038S16',
                    ]
sessionBlksWG3038 = [ 
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
                    ]

sessionDirsWG3040 = [
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S01',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S02',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S03',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S04',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S05',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S06',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S07',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S08',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S09',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S10',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S11',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S12',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S13',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S14',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S15',
#                    'E:\\Data\\Endoscope\\WG3040\\WG3040S16',
                    ]
sessionBlksWG3040 = [ 
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
                    ]

sessionDirsWG3041 = [
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S01',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S02',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S03',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S04',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S05',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S06',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S07',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S08',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S09',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S10',
#                    'E:\\Data\\Endoscope\\WG3041\\WG3041S11',
                    'E:\\Data\\Endoscope\\WG3041\\WG3041S13',
                    'E:\\Data\\Endoscope\\WG3041\\WG3041S14',
                    'E:\\Data\\Endoscope\\WG3041\\WG3041S15',
                    'E:\\Data\\Endoscope\\WG3041\\WG3041S16',
                    'E:\\Data\\Endoscope\\WG3041\\WG3041S17',
                    'E:\\Data\\Endoscope\\WG3041\\WG3041S18',
                    ]
sessionBlksWG3041 = [ 
#                    [1],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
#                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    ]

sessionDirsTH42891 = [
#                    'E:\Data\Endoscope\TH42891\TH42891SXD1',
#                    'E:\Data\Endoscope\TH42891\TH42891SXD2',
#                    'E:\Data\Endoscope\TH42891\TH42891SXD3',
#                    'E:\Data\Endoscope\TH42891\TH42891SXD4',
                    ]

sessionBlksTH42891 = [ 
#                    [4],
#                    [4],
#                    [2],
#                    [2],
                    ]

sessionDirsWG1301 = [
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S04',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S05',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S06',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S07',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S08',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S09',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S10',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S11',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S12',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S13',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S14',
                    'E:\\Data\\Endoscope\\WG1301\\WG1301S15',
                    ]
sessionBlksWG1301 = [ 
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    ]

sessionDirsWG1302 = [
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S04',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S05',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S06',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S07',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S08',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S09',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S10',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S11',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S12',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S13',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S14',
                    'E:\\Data\\Endoscope\\WG1302\\WG1302S15',
                    ]
sessionBlksWG1302 = [ 
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    ]

sessionDirsWG1304 = [
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S01',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S02',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S03',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S04',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S05',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S06',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S07',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S08',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S09',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S10',
                    'E:\\Data\\Endoscope\\WG1304\\WG1304S11',
                    ]
sessionBlksWG1304 = [ 
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    ]

sessionDirsWG3536 = [
                    'E:\\Data\\Endoscope\\WG3536\\WG3536S01',
                    'E:\\Data\\Endoscope\\WG3536\\WG3536S02',
                    'E:\\Data\\Endoscope\\WG3536\\WG3536S03',
                    'E:\\Data\\Endoscope\\WG3536\\WG3536S04',
                    ]
sessionBlksWG3536 = [ 
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    ]


animalSessionList = [sessionDirsJZ207, sessionDirsJZ209, sessionDirsJZ211, 
                     sessionDirsJZ218, sessionDirsJZ219, sessionDirsJZ222,
                     sessionDirsJZ224, sessionDirsJZ226, sessionDirsJZ229,
                     sessionDirsJZ231, sessionDirsWG027, sessionDirsWG032,
                     sessionDirsWG034, sessionDirsWG035, sessionDirsWG028,
                     sessionDirsWG029, sessionDirsWG031, sessionDirsTH42891,
                     sessionDirsWG3037,
                     sessionDirsWG3038, sessionDirsWG3040, 
                     sessionDirsWG1301, sessionDirsWG1302, sessionDirsWG1304, 
                     sessionDirsWG3041, sessionDirsWG3536]

sessionBlksList = [sessionBlksJZ207, sessionBlksJZ209, sessionBlksJZ211, 
                     sessionBlksJZ218, sessionBlksJZ219, sessionBlksJZ222,
                     sessionBlksJZ224, sessionBlksJZ226, sessionBlksJZ229,
                     sessionBlksJZ231, sessionBlksWG027, sessionBlksWG032,
                     sessionBlksWG034, sessionBlksWG035, sessionBlksWG028,
                     sessionBlksWG029, sessionBlksWG031, sessionBlksTH42891, 
                     sessionBlksWG3037,
                     sessionBlksWG3038, sessionBlksWG3040,
                     sessionBlksWG1301, sessionBlksWG1302, sessionBlksWG1304, 
                     sessionBlksWG3041, sessionBlksWG3536]

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
processID = 'Isomap_Cnorm_10Hz_Vmin0_Blks14_Rmin50_2D_10_100_5'
for animalSession, sessionBlks in zip(animalSessionList, sessionBlksList):
    for sessionDir, sessionBlk  in zip(animalSession, sessionBlks):
        sess_strs = sessionDir.split('\\')
        tempFileName = tempFolder + '\\' + sess_strs[3] + '_'+sess_strs[4]\
                        + '_' + resultName + '_' + processID + '.tmp'
        if not os.path.isfile(tempFileName):
            f = open(tempFileName, "w")
            runIsomapGrid(sessionDir, resultName, processID+'.mat', 
                          n_components = 2, velRange = [0, 1000], trainBlockList = sessionBlk, \
                          maxRespThr = 50, dataType = 'C', timeScaleDown = 3, \
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

