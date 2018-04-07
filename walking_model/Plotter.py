
from numpy import sin, cos
import numpy as np
import dynamics
import matplotlib.pyplot as plt
from math import pi
import scipy.integrate as integrate
import matplotlib.animation as animation
import Subject
from walking_model.common import * 
import math


plt.ion()

class Plotter():

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-3, 3))
        # ax = self.fig.add_subplot(111, autoscale_on=False)
        self.ax.grid()

        self.back_leg, = self.ax.plot([], [], 'bo-', lw=2)
        self.front_leg, = self.ax.plot([], [], 'ro-', lw=2)
        self.trunk, = self.ax.plot([], [], 'go-', lw=2)
        #plt.show()


    def update(self, sub):
        '''
            Update and draw the model
        '''
        points = sub.joints

        print "-"*80
        for idx,pt in enumerate(points):
            # print "points:>>",pt
            logging.info("point_{}: {}".format(idx,pt))
        print "-"*80



        x,y =  zip(*points)
        logging.info("point_fixed: {}".format([x[4],y[4]]))
        print "-"*80

        for idx,q in enumerate(sub.q):
            logging.info("q_{0}: [{2}] {1}".format(idx,math.degrees(q),JOINT_sequence[str(idx)]))
            # self.ax.text(x[idx]-x[2], y[idx], str(idx))
                    

        #back = [ _.tolist() for _ in points[:-1]]
        #flat_back = [item for sublist in back for item in sublist]
        # print "xlen:",len(x)
        # logging.info("xlen:{}".format(len(x)))

        hip_x = x[2]
        hip_y = y[2]

        self.back_leg.set_ydata([ y[:-1] ])
        self.back_leg.set_xdata([ map(lambda p:p - hip_x,x[:-1]) ])

        # self.front_leg.set_ydata([ y[:] ])
        # self.front_leg.set_xdata([ x[:] ])

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

