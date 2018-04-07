import logging
import sys
import csv
import json


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

global COMPLETED_GATE 
COMPLETED_GATE = 0

def increment_gate_count():
	global COMPLETED_GATE 
	COMPLETED_GATE+=1


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

def banner():
	print "-"*80
	print "\t "+BOLD+"WALKING MODEL"+ENDC
	print "-"*80
	logging.info(OKGREEN+"COMPLETED_GATE:{}".format(COMPLETED_GATE/2)+ENDC)

def signal_handler(signal, frame):
        logging.info('Exitting cleanly')
        sys.exit(0)
        exit()

