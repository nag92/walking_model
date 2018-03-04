#------------------------------------------------------------------------------------------#
# This file reads angle data from test.csv and updates a subject model
# Plotter is used to draw the model using matplotlib
# Subject is a model class with all attributes of the lower exoskeleton 
#------------------------------------------------------------------------------------------#
from walking_model import Plotter
from walking_model import Subject

import csv
import numpy as np
import math
import time

plotter = Plotter.Plotter()
sub = Subject.Subject()
plotter.update(sub)

joint_angle = {}
values  = []
TEST_FILE = 'bin/test.csv'
# TEST_FILE = '../test.csv'
with open(TEST_FILE) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        nums = row[1:]
        for val in nums:
            values.append(float(val))
        joint_angle[row[0]] = values
        values = []


steps =  len(joint_angle[joint_angle.keys()[1]])

while(1):
    for i in xrange(steps):

        angles = np.array([-math.radians(joint_angle['Left.Knee.Angle'][i]),
                            math.radians(joint_angle['Left.Hip.Angle'][i]),
                            math.radians(joint_angle['Right.Hip.Angle'][i]),
                           -math.radians(joint_angle['Right.Knee.Angle'][i]),
                            0,
                            0], dtype=float)

        sub.update(angles)
        plotter.update(sub)
        time.sleep(.5)

    print sub.fixed
