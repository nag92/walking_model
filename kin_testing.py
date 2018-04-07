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


plotter = Plotter.Plotter()
sub = Subject.Subject(MASS,HEIGHT)
plotter.update(sub)

joint_angle = read_csv()
steps =  len(joint_angle[joint_angle.keys()[1]])

signal.signal(signal.SIGINT, signal_handler)

while(1):
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
        time.sleep(5)

    print sub.fixed

    # break
