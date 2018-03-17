
from numpy import sin, cos
import numpy as np
import dynamics
import matplotlib.pyplot as plt
from math import pi
import scipy.integrate as integrate
import matplotlib.animation as animation
import Subject

plt.ion()

class Plotter():

    def __init__(self):
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-3, 3))
        # ax = self.fig.add_subplot(111, autoscale_on=False)
        ax.grid()

        self.back_leg, = ax.plot([], [], 'bo-', lw=2)
        self.front_leg, = ax.plot([], [], 'ro-', lw=2)
        self.trunk, = ax.plot([], [], 'go-', lw=2)
        #plt.show()


    def update(self, sub):
        '''
            Update and draw the model
        '''
        points = sub.joints

        #back = [ _.tolist() for _ in points[:-1]]
        #flat_back = [item for sublist in back for item in sublist]
        x,y =  zip(*points)
        # print "xlen:",len(x)

        self.back_leg.set_ydata([ y[:-1] ])
        self.back_leg.set_xdata([ x[:-1] ])

        # self.back_leg.set_ydata([ y[:] ])
        # self.back_leg.set_xdata([ x[:] ])

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

