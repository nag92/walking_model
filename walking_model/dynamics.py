#----------------------------------------------------------------------------------------#
# This file contains functions to compute the dynamic model of the lower limb
#----------------------------------------------------------------------------------------#

import numpy as np
from math import cos, sin
import Subject



def getTau(sub,traj):

    q = traj[0]
    qd = traj[1]
    qdd = traj[2]


def jacobain(sub):
    ''' 
      Compute the jacobian 
    '''
    l = sub._link_lengths
    m = sub._link_masses
    q = sub.q

    J = np.matrix([ [-2 * l[0] * cos(q[0]), -2 * l[1] * cos(q[1]), -2 * l[2] * cos(q[2]), 2 * l[2] * cos(q[2]), 2 * l[3] * cos(q[3])], \
                    [-2 * l[0] * sin(q[0]), -2 * l[1] * sin(q[1]), -2 * l[2] * sin(q[2]), 2 * l[2] * sin(q[2]), 2 * l[3] * sin(q[3])]])

    return J


def getM(sub):
    '''
        get MASS matrix
    '''
    l = sub._link_lengths
    m = sub._link_masses
    q = sub.q
    qd = sub.qd

    M1 =  [ (- 2*l[1]**2*m[1] - 6*l[0]**2*m[1]*cos(q[0])**2 - 24*l[0]**2*m[2]*cos(q[0])**2 - 24*l[0]**2*m[3]*cos(q[0])**2 - \
                       24*l[0]**2*m[4]*cos(q[0])**2 - 24*l[0]**2*m[5]*cos(q[0])**2 - 24*l[0]**2*m[6]*cos(q[0])**2 - \
                       6*l[0]**2*m[1]*sin(q[0])**2 - 24*l[0]**2*m[2]*sin(q[0])**2 - 24*l[0]**2*m[3]*sin(q[0])**2 - \
                       24*l[0]**2*m[4]*sin(q[0])**2 - 24*l[0]**2*m[5]*sin(q[0])**2 - 24*l[0]**2*m[6]*sin(q[0])**2), \
                      \
                      (- 12*l[0]*l[1]*m[2]*cos(q[0])*cos(q[1]) - 24*l[0]*l[1]*m[3]*cos(q[0])*cos(q[1]) - \
                       24*l[0]*l[1]*m[4]*cos(q[0])*cos(q[1]) - 24*l[0]*l[1]*m[5]*cos(q[0])*cos(q[1]) - \
                       24*l[0]*l[1]*m[6]*cos(q[0])*cos(q[1]) - 12*l[0]*l[1]*m[2]*sin(q[0])*sin(q[1]) - \
                       24*l[0]*l[1]*m[3]*sin(q[0])*sin(q[1]) - 24*l[0]*l[1]*m[4]*sin(q[0])*sin(q[1]) - \
                       24*l[0]*l[1]*m[5]*sin(q[0])*sin(q[1]) - 24*l[0]*l[1]*m[6]*sin(q[0])*sin(q[1])), \
                       \
                      (12*l[0]*l[2]*m[3]*cos(q[0])*cos(q[2]) + 24*l[0]*l[2]*m[4]*cos(q[0])*cos(q[2]) + \
                       24*l[0]*l[2]*m[5]*cos(q[0])*cos(q[2]) + 12*l[0]*l[2]*m[3]*sin(q[0])*sin(q[2]) + \
                       24*l[0]*l[2]*m[4]*sin(q[0])*sin(q[2]) + 24*l[0]*l[2]*m[5]*sin(q[0])*sin(q[2])), \
                      \
                      (12*l[0]*l[3]*m[4]*cos(q[0])*cos(q[3]) + 24*l[0]*l[3]*m[5]*cos(q[0])*cos(q[3]) + \
                       12*l[0]*l[3]*m[4]*sin(q[0])*sin(q[3]) + 24*l[0]*l[3]*m[5]*sin(q[0])*sin(q[3])), \
                      \
                      (- 12*l[0]*l[4]*m[6]*cos(q[0])*cos(q[4]) - 12*l[0]*l[4]*m[6]*sin(q[0])*sin(q[4])),\
                      \
                      0]




    M2 =  [ (-12 * l[0] * l[1] * m[2] * cos(q[0]) * cos(q[1]) - \
                        24 * l[0] * l[1] * m[3] * cos(q[0]) * cos(q[1]) - \
                       24 * l[0] * l[1] * m[4] * cos(q[0]) * cos(q[1]) - \
                       24 * l[0] * l[1] * m[5] * cos(q[0]) * cos(q[1]) - \
                       24 * l[0] * l[1] * m[6] * cos(q[0]) * cos(q[1]) - \
                       12 * l[0] * l[1] * m[2] * sin(q[0]) * sin(q[1]) - \
                       24 * l[0] * l[1] * m[3] * sin(q[0]) * sin(q[1]) - \
                       24 * l[0] * l[1] * m[4] * sin(q[0]) * sin(q[1]) - \
                       24 * l[0] * l[1] * m[5] * sin(q[0]) * sin(q[1]) - \
                       24 * l[0] * l[1] * m[6] * sin(q[0]) * sin(q[1])), \
                      \
                     (- 2 * l[2] ** 2 * m[2] - 6 * l[1] ** 2 * m[2] * cos(q[1]) ** 2 - \
                      24 * l[1] ** 2 * m[3] * cos(q[1]) ** 2 - 24 * l[1] ** 2 * m[4] * cos(q[1]) ** 2 - \
                      24 * l[1] ** 2 * m[5] * cos(q[1]) ** 2 - 24 * l[1] ** 2 * m[6] * cos(q[1]) ** 2 - \
                      6 * l[1] ** 2 * m[2] * sin(q[1]) ** 2 - 24 * l[1] ** 2 * m[3] * sin(q[1]) ** 2 - \
                      24 * l[1] ** 2 * m[4] * sin(q[1]) ** 2 - 24 * l[1] ** 2 * m[5] * sin(q[1]) ** 2 - \
                      24 * l[1] ** 2 * m[6] * sin(q[1]) ** 2) ,  \
                      \
                     (12 * l[1] * l[2] * m[3] * cos(q[1]) * cos(q[2]) + \
                      24 * l[1] * l[2] * m[4] * cos(q[1]) * cos(q[2]) + 24 * l[1] * l[2] * m[5] * cos(q[1]) * cos(q[2]) + \
                      12 * l[1] * l[2] * m[3] * sin(q[1]) * sin(q[2]) + 24 * l[1] * l[2] * m[4] * sin(q[1]) * sin(q[2]) + \
                      24 * l[1] * l[2] * m[5] * sin(q[1]) * sin(q[2])), \
                     (12 * l[1] * l[3] * m[4] * cos(q[1]) * cos(q[3]) + 24 * l[1] * l[3] * m[5] * cos(q[1]) * cos(q[3]) + \
                      12 * l[1] * l[3] * m[4] * sin(q[1]) * sin(q[3]) + 24 * l[1] * l[3] * m[5] * sin(q[1]) * sin(q[3])),\
                   (- 12 * l[1] * l[4] * m[6] * cos(q[1]) * cos(q[4]) - 12 * l[1] * l[4] * m[6] * sin(q[1]) * sin(q[4])),0]

    M3 = [ (12 * l[0] * l[2] * m[3] * cos(q[0]) * cos(q[2]) + 24 * l[0] * l[2] * m[4] * cos(q[0]) * cos(q[2]) + \
                      24 * l[0] * l[2] * m[5] * cos(q[0]) * cos(q[2]) + 12 * l[0] * l[2] * m[3] * sin(q[0]) * sin(q[2]) + \
                      24 * l[0] * l[2] * m[4] * sin(q[0]) * sin(q[2]) + 24 * l[0] * l[2] * m[5] * sin(q[0]) * sin(q[2])),\
                     (12 * l[1] * l[2] * m[3] * cos(q[1]) * cos(q[2]) + 24 * l[1] * l[2] * m[4] * cos(q[1]) * cos(q[2]) + \
                      24 * l[1] * l[2] * m[5] * cos(q[1]) * cos(q[2]) + 12 * l[1] * l[2] * m[3] * sin(q[1]) * sin(q[2]) + \
                      24 * l[1] * l[2] * m[4] * sin(q[1]) * sin(q[2]) + 24 * l[1] * l[2] * m[5] * sin(q[1]) * sin(q[2])),\
                     \
                     (- 2 * l[3] ** 2 * m[3] - 6 * l[2] ** 2 * m[3] * cos(q[2]) ** 2 - 24 * l[2] ** 2 * m[4] * cos(q[2]) ** 2 -
                      24 * l[2] ** 2 * m[5] * cos(q[2]) ** 2 - 6 * l[2] ** 2 * m[3] * sin(q[2]) ** 2 - \
                      24 * l[2] ** 2 * m[4] * sin(q[2]) ** 2 - 24 * l[2] ** 2 * m[5] * sin(q[2]) ** 2) , \
                     \
                     (- 12 * l[2] * l[3] * m[4] * cos(q[2]) * cos(q[3]) - 24 * l[2] * l[3] * m[5] * cos(q[2]) * cos(q[3]) -
                      12 * l[2] * l[3] * m[4] * sin(q[2]) * sin(q[3]) - 24 * l[2] * l[3] * m[5] * sin(q[2]) * sin(q[3])),\
                      0,0]


    M4 = [(12 * l[0] * l[3] * m[4] * cos(q[0]) * cos(q[3]) + 24 * l[0] * l[3] * m[5] * cos(q[0]) * cos(q[3]) + \
           12 * l[0] * l[3] * m[4] * sin(q[0]) * sin(q[3]) + 24 * l[0] * l[3] * m[5] * sin(q[0]) * sin(q[3])), \
          (12 * l[1] * l[3] * m[4] * cos(q[1]) * cos(q[3]) + 24 * l[1] * l[3] * m[5] * cos(q[1]) * cos(q[3]) + \
           12 * l[1] * l[3] * m[4] * sin(q[1]) * sin(q[3]) + 24 * l[1] * l[3] * m[5] * sin(q[1]) * sin(q[3])) ,\
        (- 12 * l[2] * l[3] * m[4] * cos(q[2]) * cos(q[3]) - 24 * l[2] * l[3] * m[5] * cos(q[2]) * cos(q[3]) - \
           12 * l[2] * l[3] * m[4] * sin(q[2]) * sin(q[3]) - 24 * l[2] * l[3] * m[5] * sin(q[2]) * sin(q[3])),
         (- 2 * l[4] ** 2 * m[4] - 6 * l[3] ** 2 * m[4] * cos(q[3]) ** 2 - 24 * l[3] ** 2 * m[5] * cos(q[3]) ** 2 - \
            6 * l[3] ** 2 * m[4] * sin(q[3]) ** 2 - 24 * l[3] ** 2 * m[5] * sin(q[3]) ** 2), \
            0,\
            0]


    M5 = [(- 12*l[0]*l[4]*m[6]*cos(q[0])*cos(q[4]) - 12*l[0]*l[4]*m[6]*sin(q[0])*sin(q[4])),\
         (- 12*l[1]*l[4]*m[6]*cos(q[1])*cos(q[4]) - 12*l[1]*l[4]*m[6]*sin(q[1])*sin(q[4])),\
         0,
         0,
         (- 6*m[6]*l[4]**2*cos(q[4])**2 - 6*m[6]*l[4]**2*sin(q[4])**2 - 2*m[5]*l[5]**2),
         0]


    M6 = [0,0,0,0,0,(-2*l[6]**2*m[6])]

    M = np.matrix([M1,M2,M3,M4,M5,M6])
    return M

# def getM(subject):
#
#     M1 = \
#         12 * l[0] * l[2] * m[3] * qdd3 * cos(q[0]) * cos(q[2]) - 6 * l[0] ** 2 * m[1] * qdd1 * cos(q[0]) ** 2 - \
#         24 * l[0] ** 2 * m[2] * qdd1 * cos(q[0])**2 - 24 * l[0]**2 * m[3] * qdd1 * cos(q[0]) ** 2 - \
#         24 * l[0] ** 2 * m[4] * qdd1 * cos(q[0]) ** 2 - 24 * l[0] ** 2 * m[5] * qdd1 * cos(q[0]) ** 2 - \
#         24 * l[0] ** 2 * m[6] * qdd1 * cos(q[0]) ** 2 - 6 * l[0] ** 2 * m[1] * qdd1 * sin(q[0]) ** 2 - \
#         24 * l[0] ** 2 * m[2] * qdd1 * sin(q[0]) ** 2 - 24 * l[0] ** 2 * m[3] * qdd1 * sin(q[0]) ** 2 - \
#         24 * l[0] ** 2 * m[4] * qdd1 * sin(q[0]) ** 2 - 24 * l[0] ** 2 * m[5] * qdd1 * sin(q[0]) ** 2 - \
#         24 * l[0] ** 2 * m[6] * qdd1 * sin(q[0]) ** 2 - 12 * l[0] * l[1] * m[2] * qdd2 * cos(q[0]) * cos(q[1]) - \
#         24 * l[0] * l[1] * m[3] * qdd2 * cos(q[0]) * cos(q[1]) - 24 * l[0] * l[1] * m[4] * qdd2 * cos(q[0]) * cos(q[1]) - \
#         24 * l[0] * l[1] * m[5] * qdd2 * cos(q[0]) * cos(q[1]) - 24 * l[0] * l[1] * m[6] * qdd2 * cos(q[0]) * cos(q[1]) - \
#         2 * l[1] ** 2 * m[1] * qdd1 + 24 * l[0] * l[2] * m[4] * qdd3 * cos(q[0]) * cos(q[2]) + \
#         24 * l[0] * l[2] * m[5] * qdd3 * cos(q[0]) * cos(q[2]) + 12 * l[0] * l[3] * m[4] * qdd4 * cos(q[0]) * cos(q[3]) + \
#         24 * l[0] * l[3] * m[5] * qdd4 * cos(q[0]) * cos(q[3]) - 12 * l[0] * l[4] * m[6] * qdd5 * cos(q[0]) * cos(q[4]) - \
#         12 * l[0] * l[1] * m[2] * qdd2 * sin(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[3] * qdd2 * sin(q[0]) * sin(q[1]) - \
#         24 * l[0] * l[1] * m[4] * qdd2 * sin(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[5] * qdd2 * sin(q[0]) * sin(q[1]) - \
#         24 * l[0] * l[1] * m[6] * qdd2 * sin(q[0]) * sin(q[1]) + 12 * l[0] * l[2] * m[3] * qdd3 * sin(q[0]) * sin(q[2]) + \
#         24 * l[0] * l[2] * m[4] * qdd3 * sin(q[0]) * sin(q[2]) + 24 * l[0] * l[2] * m[5] * qdd3 * sin(q[0]) * sin(q[2]) + \
#         12 * l[0] * l[3] * m[4] * qdd4 * sin(q[0]) * sin(q[3]) + 24 * l[0] * l[3] * m[5] * qdd4 * sin(q[0]) * sin(q[3]) - \
#         12 * l[0] * l[4] * m[6] * qdd5 * sin(q[0]) * sin(q[4])
#
#     M2 = \
#         12 * l[1] * l[2] * m[3] * qdd3 * cos(q[1]) * cos(q[2]) - 6 * l[1] ** 2 * m[2] * qdd2 * cos(q[1]) ** 2 - \
#         24 * l[1] ** 2 * m[3] * qdd2 * cos(q[1]) ** 2 - 24 * l[1] ** 2 * m[4] * qdd2 * cos(q[1]) ** 2 - \
#         24 * l[1] ** 2 * m[5] * qdd2 * cos(q[1]) ** 2 - 24 * l[1] ** 2 * m[6] * qdd2 * cos(q[1]) ** 2 - \
#         6 * l[1] ** 2 * m[2] * qdd2 * sin(q[1]) ** 2 - 24 * l[1] ** 2 * m[3] * qdd2 * sin(q[1]) ** 2 - \
#         24 * l[1] ** 2 * m[4] * qdd2 * sin(q[1]) ** 2 - 24 * l[1] ** 2 * m[5] * qdd2 * sin(q[1]) ** 2 - \
#         24 * l[1] ** 2 * m[6] * qdd2 * sin(q[1]) ** 2 - 12 * l[0] * l[1] * m[2] * qdd1 * cos(q[0]) * cos(q[1]) - \
#         24 * l[0] * l[1] * m[3] * qdd1 * cos(q[0]) * cos(q[1]) - 24 * l[0] * l[1] * m[4] * qdd1 * cos(q[0]) * cos(q[1]) - \
#         24 * l[0] * l[1] * m[5] * qdd1 * cos(q[0]) * cos(q[1]) - 24 * l[0] * l[1] * m[6] * qdd1 * cos(q[0]) * cos(q[1]) - \
#         2 * l[2] ** 2 * m[2] * qdd2 + 24 * l[1] * l[2] * m[4] * qdd3 * cos(q[1]) * cos(q[2]) + \
#         24 * l[1] * l[2] * m[5] * qdd3 * cos(q[1]) * cos(q[2]) + 12 * l[1] * l[3] * m[4] * qdd4 * cos(q[1]) * cos(q[3]) + \
#         24 * l[1] * l[3] * m[5] * qdd4 * cos(q[1]) * cos(q[3]) - 12 * l[1] * l[4] * m[6] * qdd5 * cos(q[1]) * cos(q[4]) - \
#         12 * l[0] * l[1] * m[2] * qdd1 * sin(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[3] * qdd1 * sin(q[0]) * sin(q[1]) - \
#         24 * l[0] * l[1] * m[4] * qdd1 * sin(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[5] * qdd1 * sin(q[0]) * sin(q[1]) - \
#         24 * l[0] * l[1] * m[6] * qdd1 * sin(q[0]) * sin(q[1]) + 12 * l[1] * l[2] * m[3] * qdd3 * sin(q[1]) * sin(q[2]) + \
#         24 * l[1] * l[2] * m[4] * qdd3 * sin(q[1]) * sin(q[2]) + 24 * l[1] * l[2] * m[5] * qdd3 * sin(q[1]) * sin(q[2]) + \
#         12 * l[1] * l[3] * m[4] * qdd4 * sin(q[1]) * sin(q[3]) + 24 * l[1] * l[3] * m[5] * qdd4 * sin(q[1]) * sin(q[3]) - \
#         12 * l[1] * l[4] * m[6] * qdd5 * sin(q[1]) * sin(q[4])
#
#     M3 = \
#         12 * l[0] * l[2] * m[3] * qdd1 * cos(q[0]) * cos(q[2]) - 6 * l[2] ** 2 * m[3] * qdd3 * cos(q[2]) ** 2 - \
#         24 * l[2] ** 2 * m[4] * qdd3 * cos(q[2]) ** 2 - 24 * l[2] ** 2 * m[5] * qdd3 * cos(q[2]) ** 2 - \
#         6 * l[2] ** 2 * m[3] * qdd3 * sin(q[2]) ** 2 - 24 * l[2] ** 2 * m[4] * qdd3 * sin(q[2]) ** 2 - \
#         24 * l[2] ** 2 * m[5] * qdd3 * sin(q[2]) ** 2 - 2 * l[3] ** 2 * m[3] * qdd3 + \
#         24 * l[0] * l[2] * m[4] * qdd1 * cos(q[0]) * cos(q[2]) + \
#         24 * l[0] * l[2] * m[5] * qdd1 * cos(q[0]) * cos(q[2]) + 12 * l[1] * l[2] * m[3] * qdd2 * cos(q[1]) * cos(q[2]) + \
#         24 * l[1] * l[2] * m[4] * qdd2 * cos(q[1]) * cos(q[2]) + 24 * l[1] * l[2] * m[5] * qdd2 * cos(q[1]) * cos(q[2]) - \
#         12 * l[2] * l[3] * m[4] * qdd4 * cos(q[2]) * cos(q[3]) - 24 * l[2] * l[3] * m[5] * qdd4 * cos(q[2]) * cos(q[3]) + \
#         12 * l[0] * l[2] * m[3] * qdd1 * sin(q[0]) * sin(q[2]) + 24 * l[0] * l[2] * m[4] * qdd1 * sin(q[0]) * sin(q[2]) + \
#         24 * l[0] * l[2] * m[5] * qdd1 * sin(q[0]) * sin(q[2]) + 12 * l[1] * l[2] * m[3] * qdd2 * sin(q[1]) * sin(q[2]) + \
#         24 * l[1] * l[2] * m[4] * qdd2 * sin(q[1]) * sin(q[2]) + 24 * l[1] * l[2] * m[5] * qdd2 * sin(q[1]) * sin(q[2]) - \
#         12 * l[2] * l[3] * m[4] * qdd4 * sin(q[2]) * sin(q[3]) - 24 * l[2] * l[3] * m[5] * qdd4 * sin(q[2]) * sin(q[3])
#     M4 = \
#         12 * l[0] * l[3] * m[4] * qdd1 * cos(q[0]) * cos(q[3]) - 6 * l[3] ** 2 * m[4] * qdd4 * cos(q[3]) ** 2 - \
#         24 * l[3] ** 2 * m[5] * qdd4 * cos(q[3]) ** 2 - 6 * l[3] ** 2 * m[4] * qdd4 * sin(q[3]) ** 2 - \
#         24 * l[3] ** 2 * m[5] * qdd4 * sin(q[3]) ** 2 - 2 * l[4] ** 2 * m[4] * qdd4 + \
#         24 * l[0] * l[3] * m[5] * qdd1 * cos(q[0]) * cos(q[3]) + 12 * l[1] * l[3] * m[4] * qdd2 * cos(q[1]) * cos(q[3]) + \
#         24 * l[1] * l[3] * m[5] * qdd2 * cos(q[1]) * cos(q[3]) - 12 * l[2] * l[3] * m[4] * qdd3 * cos(q[2]) * cos(q[3]) - \
#         24 * l[2] * l[3] * m[5] * qdd3 * cos(q[2]) * cos(q[3]) + 12 * l[0] * l[3] * m[4] * qdd1 * sin(q[0]) * sin(q[3]) + \
#         24 * l[0] * l[3] * m[5] * qdd1 * sin(q[0]) * sin(q[3]) + 12 * l[1] * l[3] * m[4] * qdd2 * sin(q[1]) * sin(q[3]) + \
#         24 * l[1] * l[3] * m[5] * qdd2 * sin(q[1]) * sin(q[3]) - 12 * l[2] * l[3] * m[4] * qdd3 * sin(q[2]) * sin(q[3]) - \
#         24 * l[2] * l[3] * m[5] * qdd3 * sin(q[2]) * sin(q[3])
#
#
#     M5 = \
#         -2 * l[5] ** 2 * m[5] * qdd5 - 6 * l[4] ** 2 * m[6] * qdd5 * cos(q[4]) ** 2 -\
#         6 * l[4] ** 2 * m[6] * qdd5 * sin(q[4]) ** 2 - 12 * l[0] * l[4] * m[6] * qdd1 * cos(q[0]) * cos(q[4]) - \
#         12 * l[1] * l[4] * m[6] * qdd2 * cos(q[1]) * cos(q[4]) - 12 * l[0] * l[4] * m[6] * qdd1 * sin(q[0]) * sin(q[4]) - \
#         12 * l[1] * l[4] * m[6] * qdd2 * sin(q[1]) * sin(q[4])
#
#
#     M6 = -2 * l[6] ** 2 * m[6] * qdd6


def getC(sub):
    '''
        get Coriolis Matrix
    '''

    l = sub._link_lengths
    m = sub._link_masses
    q = sub.q
    qd = sub.qd

    C1 = \
        12 * l[0] * l[1] * m[2] * qd[1] ** 2 * cos(q[0]) * sin(q[1]) - 12 * l[0] * l[1] * m[2] * qd[1] ** 2 * cos(q[1]) * sin(q[0]) + \
        24 * l[0] * l[1] * m[3] * qd[1] ** 2 * cos(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[3] * qd[1] ** 2 * cos(q[1]) * sin(q[0]) + \
        24 * l[0] * l[1] * m[4] * qd[1] ** 2 * cos(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[4] * qd[1] ** 2 * cos(q[1]) * sin(q[0]) + \
        24 * l[0] * l[1] * m[5] * qd[1] ** 2 * cos(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[5] * qd[1] ** 2 * cos(q[1]) * sin(q[0]) + \
        24 * l[0] * l[1] * m[6] * qd[1] ** 2 * cos(q[0]) * sin(q[1]) - 24 * l[0] * l[1] * m[6] * qd[1] ** 2 * cos(q[1]) * sin(q[0]) - \
        12 * l[0] * l[2] * m[3] * qd[2] ** 2 * cos(q[0]) * sin(q[2]) + 12 * l[0] * l[2] * m[3] * qd[2] ** 2 * cos(q[2]) * sin(q[0]) - \
        24 * l[0] * l[2] * m[4] * qd[2] ** 2 * cos(q[0]) * sin(q[2]) + 24 * l[0] * l[2] * m[4] * qd[2] ** 2 * cos(q[2]) * sin(q[0]) - \
        24 * l[0] * l[2] * m[5] * qd[2] ** 2 * cos(q[0]) * sin(q[2]) + 24 * l[0] * l[2] * m[5] * qd[2] ** 2 * cos(q[2]) * sin(q[0]) - \
        12 * l[0] * l[3] * m[4] * qd[3] ** 2 * cos(q[0]) * sin(q[3]) + 12 * l[0] * l[3] * m[4] * qd[3] ** 2 * cos(q[3]) * sin(q[0]) - \
        24 * l[0] * l[3] * m[5] * qd[3] ** 2 * cos(q[0]) * sin(q[3]) + 24 * l[0] * l[3] * m[5] * qd[3] ** 2 * cos(q[3]) * sin(q[0]) + \
        12 * l[0] * l[4] * m[6] * qd[4] ** 2 * cos(q[0]) * sin(q[4]) - 12 * l[0] * l[4] * m[6] * qd[4] ** 2 * cos(q[4]) * sin(q[0])

    C2 = \
        12 * l[0] * l[1] * m[2] * qd[0] ** 2 * cos(q[1]) * sin(q[0]) - 12 * l[0] * l[1] * m[2] * qd[0] ** 2 * cos(q[0]) * sin(q[1]) - \
        24 * l[0] * l[1] * m[3] * qd[0] ** 2 * cos(q[0]) * sin(q[1]) + 24 * l[0] * l[1] * m[3] * qd[0] ** 2 * cos(q[1]) * sin(q[0]) - \
        24 * l[0] * l[1] * m[4] * qd[0] ** 2 * cos(q[0]) * sin(q[1]) + 24 * l[0] * l[1] * m[4] * qd[0] ** 2 * cos(q[1]) * sin(q[0]) - \
        24 * l[0] * l[1] * m[5] * qd[0] ** 2 * cos(q[0]) * sin(q[1]) + 24 * l[0] * l[1] * m[5] * qd[0] ** 2 * cos(q[1]) * sin(q[0]) - \
        24 * l[0] * l[1] * m[6] * qd[0] ** 2 * cos(q[0]) * sin(q[1]) + 24 * l[0] * l[1] * m[6] * qd[0] ** 2 * cos(q[1]) * sin(q[0]) - \
        12 * l[1] * l[2] * m[3] * qd[2] ** 2 * cos(q[1]) * sin(q[2]) + 12 * l[1] * l[2] * m[3] * qd[2] ** 2 * cos(q[2]) * sin(q[1]) - \
        24 * l[1] * l[2] * m[4] * qd[2] ** 2 * cos(q[1]) * sin(q[2]) + 24 * l[1] * l[2] * m[4] * qd[2] ** 2 * cos(q[2]) * sin(q[1]) - \
        24 * l[1] * l[2] * m[5] * qd[2] ** 2 * cos(q[1]) * sin(q[2]) + 24 * l[1] * l[2] * m[5] * qd[2] ** 2 * cos(q[2]) * sin(q[1]) - \
        12 * l[1] * l[3] * m[4] * qd[3] ** 2 * cos(q[1]) * sin(q[3]) + 12 * l[1] * l[3] * m[4] * qd[3] ** 2 * cos(q[3]) * sin(q[1]) - \
        24 * l[1] * l[3] * m[5] * qd[3] ** 2 * cos(q[1]) * sin(q[3]) + 24 * l[1] * l[3] * m[5] * qd[3] ** 2 * cos(q[3]) * sin(q[1]) + \
        12 * l[1] * l[4] * m[6] * qd[4] ** 2 * cos(q[1]) * sin(q[4]) - 12 * l[1] * l[4] * m[6] * qd[4] ** 2 * cos(q[4]) * sin(q[1])

    C3 = \
        12 * l[0] * l[2] * m[3] * qd[0] ** 2 * cos(q[0]) * sin(q[2]) - 12 * l[0] * l[2] * m[3] * qd[0] ** 2 * cos(q[2]) * sin(q[0]) + \
        24 * l[0] * l[2] * m[4] * qd[0] ** 2 * cos(q[0]) * sin(q[2]) - 24 * l[0] * l[2] * m[4] * qd[0] ** 2 * cos(q[2]) * sin(q[0]) + \
        24 * l[0] * l[2] * m[5] * qd[0] ** 2 * cos(q[0]) * sin(q[2]) - 24 * l[0] * l[2] * m[5] * qd[0] ** 2 * cos(q[2]) * sin(q[0]) + \
        12 * l[1] * l[2] * m[3] * qd[1] ** 2 * cos(q[1]) * sin(q[2]) - 12 * l[1] * l[2] * m[3] * qd[1] ** 2 * cos(q[2]) * sin(q[1]) + \
        24 * l[1] * l[2] * m[4] * qd[1] ** 2 * cos(q[1]) * sin(q[2]) - 24 * l[1] * l[2] * m[4] * qd[1] ** 2 * cos(q[2]) * sin(q[1]) + \
        24 * l[1] * l[2] * m[5] * qd[1] ** 2 * cos(q[1]) * sin(q[2]) - 24 * l[1] * l[2] * m[5] * qd[1] ** 2 * cos(q[2]) * sin(q[1]) + \
        12 * l[2] * l[3] * m[4] * qd[3] ** 2 * cos(q[2]) * sin(q[3]) - 12 * l[2] * l[3] * m[4] * qd[3] ** 2 * cos(q[3]) * sin(q[2]) + \
        24 * l[2] * l[3] * m[5] * qd[3] ** 2 * cos(q[2]) * sin(q[3]) - 24 * l[2] * l[3] * m[5] * qd[3] ** 2 * cos(q[3]) * sin(q[2])


    C4 = \
        12 * l[0] * l[3] * m[4] * qd[0] ** 2 * cos(q[0]) * sin(q[3]) - 12 * l[0] * l[3] * m[4] * qd[0] ** 2 * cos(q[3]) * sin(q[0]) + \
        24 * l[0] * l[3] * m[5] * qd[0] ** 2 * cos(q[0]) * sin(q[3]) - 24 * l[0] * l[3] * m[5] * qd[0] ** 2 * cos(q[3]) * sin(q[0]) + \
        12 * l[1] * l[3] * m[4] * qd[1] ** 2 * cos(q[1]) * sin(q[3]) - 12 * l[1] * l[3] * m[4] * qd[1] ** 2 * cos(q[3]) * sin(q[1]) + \
        24 * l[1] * l[3] * m[5] * qd[1] ** 2 * cos(q[1]) * sin(q[3]) - 24 * l[1] * l[3] * m[5] * qd[1] ** 2 * cos(q[3]) * sin(q[1]) - \
        12 * l[2] * l[3] * m[4] * qd[2] ** 2 * cos(q[2]) * sin(q[3]) + 12 * l[2] * l[3] * m[4] * qd[2] ** 2 * cos(q[3]) * sin(q[2]) - \
        24 * l[2] * l[3] * m[5] * qd[2] ** 2 * cos(q[2]) * sin(q[3]) + 24 * l[2] * l[3] * m[5] * qd[2] ** 2 * cos(q[3]) * sin(q[2])


    C5 = \
        12 * l[0] * l[4] * m[6] * qd[0] ** 2 * cos(q[4]) * sin(q[0]) - 12 * l[0] * l[4] * m[6] * qd[0] ** 2 * cos(q[0]) * sin(q[4]) - \
        12 * l[1] * l[4] * m[6] * qd[1] ** 2 * cos(q[1]) * sin(q[4]) + 12 * l[1] * l[4] * m[6] * qd[1] ** 2 * cos(q[4]) * sin(q[1])


    C6 = 0

    C = np.matrix([C1, C2, C3, C4, C5, C6])
    return C

def getG(sub):
    '''
        get Gravity Matrix
    '''

    l = sub._link_lengths
    m = sub._link_masses
    q = sub.q
    qd = sub.qd

    G1 =  10 * l[0] * cos(q[0]) + 10 * l[0] * sin(q[0])
    G2 =  8 * l[1] * cos(q[1]) + 8 * l[1] * sin(q[1])
    G3 = -4 * l[2] * cos(q[2]) - 4 * l[2] * sin(q[2])
    G4 = - 2 * l[3] * cos(q[3]) - 2 * l[3] * sin(q[3])
    G5 = 2 * l[4] * cos(q[4]) + 2 * l[4] * sin(q[4])
    G6 = 0
    G = np.matrix([G1, G2, G3, G4, G5, G6])
    return G



def FK(sub):
    '''
        Compute Forward Kinematics
    '''
    q = sub.q
    l = sub._link_lengths
    P = []
    P.append(sub.fixed)
    Q = []

    for i in xrange(1,6):

        temp = []
        R = np.matrix([ [cos(q[i - 1]), -sin(q[i - 1])], [ sin(q[i - 1]), cos(q[i - 1] ) ] ] )

        if i == 1 or i == 2:
            temp = P[i - 1] + R * np.matrix( [ [0], [ 2 * l[i - 1] ]])
        elif i == 4 or i == 3:
            temp = P[ i - 1] + R * np.matrix( [ [0], [ -2 * l[i - 1] ]])
        elif i == 5:
            temp = P[2] + R * np.matrix( [ [0], [ 2 * l[i - 1] ]])
        P.append(temp)

    P = [ temp.tolist() for  temp in P    ]

    flatten = lambda l: [item for sublist in l for item in sublist]
    P = [ flatten(temp) for temp in P]

    return P




