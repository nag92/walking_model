
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
import traceback


plt.ion()

class Plotter():

    def __init__(self):
        self.fig = plt.figure()
        self.fig2 = plt.figure()

        self.ax = self.fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-3, 3))
        
        self.ax0 = self.fig2.add_subplot(611, autoscale_on=True)
        self.ax1 = self.fig2.add_subplot(612, autoscale_on=True)
        self.ax2 = self.fig2.add_subplot(613, autoscale_on=True)
        self.ax3 = self.fig2.add_subplot(614, autoscale_on=True)
        self.ax4 = self.fig2.add_subplot(615, autoscale_on=True)
        self.ax5 = self.fig2.add_subplot(616, autoscale_on=True)
        
        # ax = self.fig.add_subplot(111, autoscale_on=False)
        self.ax.grid()

        self.back_leg, = self.ax.plot([], [], 'bo-', lw=2)
        self.front_leg, = self.ax.plot([], [], 'ro-', lw=2)
        self.trunk, = self.ax.plot([], [], 'go-', lw=2)
        
        self.ax0.grid()
        self.ax1.grid()
        self.ax2.grid()
        self.ax3.grid()
        self.ax4.grid()
        self.ax5.grid()

        #plt.show()
        self.buffer = {
                        "tau_0":[],
                        "tau_1":[],
                        "tau_2":[],
                        "tau_3":[],
                        "tau_4":[],
                        "tau_5":[],
                        }


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
       
        try:
            for idx,tau in enumerate(sub.tau):
                logging.info("tau_{0}: [{2}] {1}".format(idx,tau.tolist()[0][0],JOINT_sequence[str(idx)]))        
                self.buffer["tau_{}".format(idx)].append(tau.tolist()[0][0])
        except:
            pass
        
        hip_x = x[2]
        hip_y = y[2]

        Y_data = y[:-1]
        # print(Y_data)
        X_data = map(lambda p:p - hip_x,x[:-1])

        # X_data,Y_data = self.get_feet(X_data, Y_data, sub)

        self.back_leg.set_ydata([ Y_data ])
        self.back_leg.set_xdata([ X_data ])

        try:
            # print(self.buffer)
            # print(range(len(self.buffer)))

            self.ax0.plot(range(len(self.buffer["tau_0"])),self.buffer["tau_0"],'b')
            self.ax1.plot(range(len(self.buffer["tau_1"])),self.buffer["tau_1"],'b')
            self.ax2.plot(range(len(self.buffer["tau_2"])),self.buffer["tau_2"],'b')
            self.ax3.plot(range(len(self.buffer["tau_3"])),self.buffer["tau_3"],'b')
            self.ax4.plot(range(len(self.buffer["tau_4"])),self.buffer["tau_4"],'b')
            self.ax5.plot(range(len(self.buffer["tau_5"])),self.buffer["tau_5"],'b')

        except Exception as e:
            traceback.print_exc()
            pass

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



