
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
                    

        print "-"*80
        # for idx,tau in enumerate(sub.tau):
            # logging.info("tau_{0}: [{2}] {1}".format(idx,tau,JOINT_sequence[str(idx)]))        

        print(sub.tau)
        print(sub.tau.shape)
        #back = [ _.tolist() for _ in points[:-1]]
        #flat_back = [item for sublist in back for item in sublist]
        # print "xlen:",len(x)
        # logging.info("xlen:{}".format(len(x)))

        hip_x = x[2]
        hip_y = y[2]

        Y_data = y[:-1]
        X_data = map(lambda p:p - hip_x,x[:-1])

        # X_data,Y_data = self.get_feet(X_data, Y_data, sub)

        self.back_leg.set_ydata([ Y_data ])
        self.back_leg.set_xdata([ X_data ])

        # self.front_leg.set_ydata([ y[:] ])
        # self.front_leg.set_xdata([ x[:] ])

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def get_feet(self,X_data,Y_data,sub):
        left_ankle_angle = np.pi - sub.q[4]
        right_ankle_angle = np.pi -  sub.q[5]

        left_ankle_pt = (X_data[0],Y_data[0])
        right_ankle_pt = (X_data[0],Y_data[0])

        l = 0.1*sub._height

        temp = l/np.sqrt(1 + np.square(np.tan(left_ankle_angle)))
        
        toe_left_x = left_ankle_pt[0] + temp
        toe_left_y = left_ankle_pt[1] + np.tan(left_ankle_angle)*temp

        temp = l/np.sqrt(1 + np.square(np.tan(right_ankle_angle)))
        toe_right_x = right_ankle_pt[0] + temp
        toe_right_y = right_ankle_pt[1] + np.tan(right_ankle_angle)*temp


        new_X_data = [toe_left_x]
        for x in X_data:
            new_X_data.append(x)
        new_X_data.append(toe_right_x)

        new_Y_data = [toe_left_y]
        for y in Y_data:
            new_Y_data.append(y)
        new_Y_data.append(toe_right_y)

        return new_X_data,new_Y_data



