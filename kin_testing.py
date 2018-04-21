#------------------------------------------------------------------------------------------#
# This file reads angle data from test.csv and updates a subject model
# Plotter is used to draw the model using matplotlib
# Subject is a model class with all attributes of the lower exoskeleton
# Authors: Nathanial G
#          Ameya Wagh - aywagh@wpi.edu 
#------------------------------------------------------------------------------------------#
from walking_model import Plotter
from walking_model import Subject
from walking_model.common import * 

import csv
import numpy as np
import math
import time
import os
import signal
import sys
import serial

PORT = '/dev/ttyACM0'
BAUDRATE = 250000

USE_SERIAL = False

plotter = Plotter.Plotter()
sub = Subject.Subject(MASS,HEIGHT)
plotter.update(sub)

if CONFIG_FILE["NEW_FORMAT"]:
    joint_angle = read_csv2()
else:
    joint_angle = read_csv()
steps =  len(joint_angle[joint_angle.keys()[1]])

# signal.signal(signal.SIGINT, signal_handler)

if not USE_SERIAL:
    while(1):
        try:
            for i in xrange(steps):
                os.system('clear')
                banner()
                angles = np.array([-math.radians(joint_angle['Left.Knee.Angle'][i]),
                                    math.radians(joint_angle['Left.Hip.Angle'][i]),
                                    math.radians(joint_angle['Right.Hip.Angle'][i]),
                                   -math.radians(joint_angle['Right.Knee.Angle'][i]),
                                    
                                    math.radians(joint_angle['Right.Ankle.Angle'][i]),
                                    math.radians(joint_angle['Left.Ankle.Angle'][i])], dtype=float)

                sub.update(angles)
                plotter.update(sub)
                # time.sleep(.5)
                # time.sleep(.005)

            print sub.fixed

            # break
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            close_all()
else:
    print("using serial")
    with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
        print("reading...")
        
        while True:
            os.system('clear')
            try:
                line = ser.readline()   # read a '\n' terminated line
                data = [float(every_data) for every_data in line.split(',')[:-1]]
                print(data)
                banner()
                angles = np.array([-math.radians(data[CALIBRATION['Left.Knee.Angle']['index']]),
                                    math.radians(data[CALIBRATION['Left.Hip.Angle']['index']]),
                                    math.radians(data[CALIBRATION['Right.Hip.Angle']['index']]),
                                   -math.radians(data[CALIBRATION['Right.Knee.Angle']['index']]),
                                    
                                    math.radians(data[CALIBRATION['Right.Ankle.Angle']['index']]),
                                    math.radians(data[CALIBRATION['Left.Ankle.Angle']['index']])], dtype=float)
                print(angles)
                sub.update(angles)
                plotter.update(sub)
            except:
                pass

        
