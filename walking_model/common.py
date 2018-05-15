import logging
import sys
import csv
import json
import time
import pprint
import signal


pp = pprint.PrettyPrinter(indent=4)

logging.basicConfig(format='[%(levelname)s]:%(message)s',level=logging.INFO)

CONFIG_FILE = json.load(open('config.json'))

# TEST_FILE = 'bin/test.csv'
TEST_FILE = CONFIG_FILE["TEST_FILE"]
MASS=CONFIG_FILE["SUBJECT"]["MASS"]
HEIGHT=CONFIG_FILE["SUBJECT"]["HEIGHT"]

JOINT_sequence=CONFIG_FILE["SUBJECT"]["JOINT_sequence"]

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

global COMPLETED_GAIT 
COMPLETED_GAIT = 0

CALIBRATION = CONFIG_FILE["SUBJECT"]["CALIBRATION"]



def increment_gait_count():
    global COMPLETED_GAIT 
    COMPLETED_GAIT+=1


def read_csv():
    joint_angle = {}
    values  = []
    with open(TEST_FILE) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            nums = row[1:]
            for val in nums:
                values.append(float(val))
            joint_angle[row[0]] = values
            values = []
    return joint_angle



def read_csv2():
    parse_csv = lambda row,idx: CALIBRATION[idx]['multiplier']*float(row[CALIBRATION[idx]['index']])+CALIBRATION[idx]['offset']  
    joint_angle = {
                    'Left.Knee.Angle':[],
                    'Left.Hip.Angle':[],
                    'Right.Hip.Angle':[],
                    'Right.Knee.Angle':[],
                    'Right.Ankle.Angle':[],
                    'Left.Ankle.Angle':[]
                    }

    indx_cnt = 0
    with open(TEST_FILE) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if indx_cnt > 5:
                # print row
                try:
                    for _key in joint_angle.keys():
                        joint_angle[_key].append(parse_csv(row,_key))
                except:
                    pass
                # print joint_angle
                # pp.pprint(joint_angle)
                # print('-'*80)
                # time.sleep(1)
            indx_cnt+=1

    return joint_angle

def banner():
	print "-"*80
	print "\t "+BOLD+"WALKING MODEL"+ENDC
	print "-"*80
	logging.info(OKGREEN+"COMPLETED_GAIT:{}".format(COMPLETED_GAIT/2)+ENDC)


class KillGracefully:
    def __init__(self):
        self.KILL_FLAG = False
        signal.signal(signal.SIGINT, self.signal_handler)
        # signal.signal(signal.SIGTSTP, self.signal_handler)

    def signal_handler(self,signal, frame):
        self.KILL_FLAG = True
        print('#'*80)
        close_all() 



def signal_handler(signal, frame):
    KILL_FLAG = True
    print('#'*80)
    close_all()    

def close_all():
    logging.info('Exitting cleanly')
    sys.exit(0)
    exit()
