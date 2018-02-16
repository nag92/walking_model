# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import scipy.integrate as integrate
import matplotlib.animation as animation

import csv

joint_angle = {}
values  = []
with open('test.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        nums = row[1:]
        for val in nums:
            values.append(float(val))
        joint_angle[row[0]] = values
        values = []


steps =  len(joint_angle[joint_angle.keys()[1]])



fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

left_leg, = ax.plot([], [], 'bo-', lw=2)
right_leg, = ax.plot([], [], 'ro-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def correctAngles(hip,knee,ankle):
    hip = hip * pi / 180 - 0.5 * pi
    knee = -knee * (pi / 180)
    ankle = ankle * pi / 180 + pi
    return hip,knee,ankle

def FK(hip,knee,ankle):
    l1 = 0.5
    l2 = 0.5
    l3 = 0.1

    hip,knee,ankle = correctAngles(hip,knee,ankle)
    x1 = l1*cos(hip)
    y1 = l1*sin(hip)

    x2 = x1 + l2 * cos(hip+knee)
    y2 = y1 + l2 * sin(hip+knee)

    x3 = x2 + l3 * cos(hip + knee + ankle)
    y3 = y2 + l3 * sin(hip + knee + ankle)

    x_data = [0,x1, x2, x3]
    y_data = [0, y1, y2, y3]
    return x_data, y_data


def init():
    left_leg.set_data([], [])
    right_leg.set_data([], [])
    time_text.set_text('')
    return left_leg,right_leg, time_text


def animate(i):


    left_x,left_y = FK(joint_angle['Left.Hip.Angle'][i],
                       joint_angle['Left.Knee.Angle'][i],
                       joint_angle['Left.Ankle.Angle'][i])

    right_x,right_y = FK(joint_angle['Right.Hip.Angle'][i],
                         joint_angle['Right.Knee.Angle'][i],
                         joint_angle['Right.Ankle.Angle'][i])


    left_leg.set_data(left_x, left_y)
    right_leg.set_data(right_x, right_y)
    time_text.set_text(time_template % (i))

    return right_leg, left_leg, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, steps),
                              interval=steps, blit=True, init_func=init)


plt.show()