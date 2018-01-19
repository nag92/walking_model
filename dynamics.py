

import numpy as np
from math import cos, sin
import subject



def getTau(sub, q,qd,qdd,):



def getM(sub):

    lengths = sub._link_lengths
    masses = sub._link_masses
    l_1 = lengths[0]
    l_2 = lengths[1]
    l_3 = lengths[2]
    l_4 = lengths[3]
    l_5 = lengths[4]
    l_6 = lengths[5]
    l_7 = lengths[6]
    m_1 = masses[0]
    m_2 = masses[1]
    m_3 = masses[2]
    m_4 = masses[3]
    m_5 = masses[4]
    m_6 = masses[5]

    M1 =  [ (- 2*l_2**2*m_2 - 6*l_1**2*m_2*cos(q1)**2 - 24*l_1**2*m_3*cos(q1)**2 - 24*l_1**2*m_4*cos(q1)**2 - \
                       24*l_1**2*m_5*cos(q1)**2 - 24*l_1**2*m_6*cos(q1)**2 - 24*l_1**2*m_7*cos(q1)**2 - \
                       6*l_1**2*m_2*sin(q1)**2 - 24*l_1**2*m_3*sin(q1)**2 - 24*l_1**2*m_4*sin(q1)**2 - \
                       24*l_1**2*m_5*sin(q1)**2 - 24*l_1**2*m_6*sin(q1)**2 - 24*l_1**2*m_7*sin(q1)**2), \
                      \
                      (- 12*l_1*l_2*m_3*cos(q1)*cos(q2) - 24*l_1*l_2*m_4*cos(q1)*cos(q2) - \
                       24*l_1*l_2*m_5*cos(q1)*cos(q2) - 24*l_1*l_2*m_6*cos(q1)*cos(q2) - \
                       24*l_1*l_2*m_7*cos(q1)*cos(q2) - 12*l_1*l_2*m_3*sin(q1)*sin(q2) - \
                       24*l_1*l_2*m_4*sin(q1)*sin(q2) - 24*l_1*l_2*m_5*sin(q1)*sin(q2) - \
                       24*l_1*l_2*m_6*sin(q1)*sin(q2) - 24*l_1*l_2*m_7*sin(q1)*sin(q2)), \
                       \
                      (12*l_1*l_3*m_4*cos(q1)*cos(q3) + 24*l_1*l_3*m_5*cos(q1)*cos(q3) + \
                       24*l_1*l_3*m_6*cos(q1)*cos(q3) + 12*l_1*l_3*m_4*sin(q1)*sin(q3) + \
                       24*l_1*l_3*m_5*sin(q1)*sin(q3) + 24*l_1*l_3*m_6*sin(q1)*sin(q3)), \
                      \
                      (12*l_1*l_4*m_5*cos(q1)*cos(q4) + 24*l_1*l_4*m_6*cos(q1)*cos(q4) + \
                       12*l_1*l_4*m_5*sin(q1)*sin(q4) + 24*l_1*l_4*m_6*sin(q1)*sin(q4)), \
                      \
                      (- 12*l_1*l_5*m_7*cos(q1)*cos(q5) - 12*l_1*l_5*m_7*sin(q1)*sin(q5)),\
                      \
                      0]




    M2 =  [ (-12 * l_1 * l_2 * m_3 * cos(q1) * cos(q2) - \
                        24 * l_1 * l_2 * m_4 * cos(q1) * cos(q2) - \
                       24 * l_1 * l_2 * m_5 * cos(q1) * cos(q2) - \
                       24 * l_1 * l_2 * m_6 * cos(q1) * cos(q2) - \
                       24 * l_1 * l_2 * m_7 * cos(q1) * cos(q2) - \
                       12 * l_1 * l_2 * m_3 * sin(q1) * sin(q2) - \
                       24 * l_1 * l_2 * m_4 * sin(q1) * sin(q2) - \
                       24 * l_1 * l_2 * m_5 * sin(q1) * sin(q2) - \
                       24 * l_1 * l_2 * m_6 * sin(q1) * sin(q2) - \
                       24 * l_1 * l_2 * m_7 * sin(q1) * sin(q2)), \
                      \
                     (- 2 * l_3 ** 2 * m_3 - 6 * l_2 ** 2 * m_3 * cos(q2) ** 2 - \
                      24 * l_2 ** 2 * m_4 * cos(q2) ** 2 - 24 * l_2 ** 2 * m_5 * cos(q2) ** 2 - \
                      24 * l_2 ** 2 * m_6 * cos(q2) ** 2 - 24 * l_2 ** 2 * m_7 * cos(q2) ** 2 - \
                      6 * l_2 ** 2 * m_3 * sin(q2) ** 2 - 24 * l_2 ** 2 * m_4 * sin(q2) ** 2 - \
                      24 * l_2 ** 2 * m_5 * sin(q2) ** 2 - 24 * l_2 ** 2 * m_6 * sin(q2) ** 2 - \
                      24 * l_2 ** 2 * m_7 * sin(q2) ** 2) ,  \
                      \
                     (12 * l_2 * l_3 * m_4 * cos(q2) * cos(q3) + \
                      24 * l_2 * l_3 * m_5 * cos(q2) * cos(q3) + 24 * l_2 * l_3 * m_6 * cos(q2) * cos(q3) + \
                      12 * l_2 * l_3 * m_4 * sin(q2) * sin(q3) + 24 * l_2 * l_3 * m_5 * sin(q2) * sin(q3) + \
                      24 * l_2 * l_3 * m_6 * sin(q2) * sin(q3)), \
                     (12 * l_2 * l_4 * m_5 * cos(q2) * cos(q4) + 24 * l_2 * l_4 * m_6 * cos(q2) * cos(q4) + \
                      12 * l_2 * l_4 * m_5 * sin(q2) * sin(q4) + 24 * l_2 * l_4 * m_6 * sin(q2) * sin(q4)),\
                   (- 12 * l_2 * l_5 * m_7 * cos(q2) * cos(q5) - 12 * l_2 * l_5 * m_7 * sin(q2) * sin(q5)),0]

    M3 = [ (12 * l_1 * l_3 * m_4 * cos(q1) * cos(q3) + 24 * l_1 * l_3 * m_5 * cos(q1) * cos(q3) + \
                      24 * l_1 * l_3 * m_6 * cos(q1) * cos(q3) + 12 * l_1 * l_3 * m_4 * sin(q1) * sin(q3) + \
                      24 * l_1 * l_3 * m_5 * sin(q1) * sin(q3) + 24 * l_1 * l_3 * m_6 * sin(q1) * sin(q3)),\
                     (12 * l_2 * l_3 * m_4 * cos(q2) * cos(q3) + 24 * l_2 * l_3 * m_5 * cos(q2) * cos(q3) + \
                      24 * l_2 * l_3 * m_6 * cos(q2) * cos(q3) + 12 * l_2 * l_3 * m_4 * sin(q2) * sin(q3) + \
                      24 * l_2 * l_3 * m_5 * sin(q2) * sin(q3) + 24 * l_2 * l_3 * m_6 * sin(q2) * sin(q3)),\
                     \
                     (- 2 * l_4 ** 2 * m_4 - 6 * l_3 ** 2 * m_4 * cos(q3) ** 2 - 24 * l_3 ** 2 * m_5 * cos(q3) ** 2 -
                      24 * l_3 ** 2 * m_6 * cos(q3) ** 2 - 6 * l_3 ** 2 * m_4 * sin(q3) ** 2 - \
                      24 * l_3 ** 2 * m_5 * sin(q3) ** 2 - 24 * l_3 ** 2 * m_6 * sin(q3) ** 2) , \
                     \
                     (- 12 * l_3 * l_4 * m_5 * cos(q3) * cos(q4) - 24 * l_3 * l_4 * m_6 * cos(q3) * cos(q4) -
                      12 * l_3 * l_4 * m_5 * sin(q3) * sin(q4) - 24 * l_3 * l_4 * m_6 * sin(q3) * sin(q4)),\
                      0,0]


    M4 = [(12 * l_1 * l_4 * m_5 * cos(q1) * cos(q4) + 24 * l_1 * l_4 * m_6 * cos(q1) * cos(q4) + \
           12 * l_1 * l_4 * m_5 * sin(q1) * sin(q4) + 24 * l_1 * l_4 * m_6 * sin(q1) * sin(q4)), \
          (12 * l_2 * l_4 * m_5 * cos(q2) * cos(q4) + 24 * l_2 * l_4 * m_6 * cos(q2) * cos(q4) + \
           12 * l_2 * l_4 * m_5 * sin(q2) * sin(q4) + 24 * l_2 * l_4 * m_6 * sin(q2) * sin(q4)) ,\
        (- 12 * l_3 * l_4 * m_5 * cos(q3) * cos(q4) - 24 * l_3 * l_4 * m_6 * cos(q3) * cos(q4) - \
           12 * l_3 * l_4 * m_5 * sin(q3) * sin(q4) - 24 * l_3 * l_4 * m_6 * sin(q3) * sin(q4)),
         (- 2 * l_5 ** 2 * m_5 - 6 * l_4 ** 2 * m_5 * cos(q4) ** 2 - 24 * l_4 ** 2 * m_6 * cos(q4) ** 2 - \
            6 * l_4 ** 2 * m_5 * sin(q4) ** 2 - 24 * l_4 ** 2 * m_6 * sin(q4) ** 2), \
            0,\
            0]


    M5 = [(- 12*l_1*l_5*m_7*cos(q1)*cos(q5) - 12*l_1*l_5*m_7*sin(q1)*sin(q5)),\
         (- 12*l_2*l_5*m_7*cos(q2)*cos(q5) - 12*l_2*l_5*m_7*sin(q2)*sin(q5)),\
         0,
         0,
         (- 6*m_7*l_5**2*cos(q5)**2 - 6*m_7*l_5**2*sin(q5)**2 - 2*m_6*l_6**2),
         0]


    M6 = [0,0,0,0,0,(-2*l_7**2*m_7)]

    M = np.matrix([M1,M2,M3,M4,M5,M6])
    return M

# def getM(subject):
#
#     M1 = \
#         12 * l_1 * l_3 * m_4 * qdd3 * cos(q1) * cos(q3) - 6 * l_1 ** 2 * m_2 * qdd1 * cos(q1) ** 2 - \
#         24 * l_1 ** 2 * m_3 * qdd1 * cos(q1)**2 - 24 * l_1**2 * m_4 * qdd1 * cos(q1) ** 2 - \
#         24 * l_1 ** 2 * m_5 * qdd1 * cos(q1) ** 2 - 24 * l_1 ** 2 * m_6 * qdd1 * cos(q1) ** 2 - \
#         24 * l_1 ** 2 * m_7 * qdd1 * cos(q1) ** 2 - 6 * l_1 ** 2 * m_2 * qdd1 * sin(q1) ** 2 - \
#         24 * l_1 ** 2 * m_3 * qdd1 * sin(q1) ** 2 - 24 * l_1 ** 2 * m_4 * qdd1 * sin(q1) ** 2 - \
#         24 * l_1 ** 2 * m_5 * qdd1 * sin(q1) ** 2 - 24 * l_1 ** 2 * m_6 * qdd1 * sin(q1) ** 2 - \
#         24 * l_1 ** 2 * m_7 * qdd1 * sin(q1) ** 2 - 12 * l_1 * l_2 * m_3 * qdd2 * cos(q1) * cos(q2) - \
#         24 * l_1 * l_2 * m_4 * qdd2 * cos(q1) * cos(q2) - 24 * l_1 * l_2 * m_5 * qdd2 * cos(q1) * cos(q2) - \
#         24 * l_1 * l_2 * m_6 * qdd2 * cos(q1) * cos(q2) - 24 * l_1 * l_2 * m_7 * qdd2 * cos(q1) * cos(q2) - \
#         2 * l_2 ** 2 * m_2 * qdd1 + 24 * l_1 * l_3 * m_5 * qdd3 * cos(q1) * cos(q3) + \
#         24 * l_1 * l_3 * m_6 * qdd3 * cos(q1) * cos(q3) + 12 * l_1 * l_4 * m_5 * qdd4 * cos(q1) * cos(q4) + \
#         24 * l_1 * l_4 * m_6 * qdd4 * cos(q1) * cos(q4) - 12 * l_1 * l_5 * m_7 * qdd5 * cos(q1) * cos(q5) - \
#         12 * l_1 * l_2 * m_3 * qdd2 * sin(q1) * sin(q2) - 24 * l_1 * l_2 * m_4 * qdd2 * sin(q1) * sin(q2) - \
#         24 * l_1 * l_2 * m_5 * qdd2 * sin(q1) * sin(q2) - 24 * l_1 * l_2 * m_6 * qdd2 * sin(q1) * sin(q2) - \
#         24 * l_1 * l_2 * m_7 * qdd2 * sin(q1) * sin(q2) + 12 * l_1 * l_3 * m_4 * qdd3 * sin(q1) * sin(q3) + \
#         24 * l_1 * l_3 * m_5 * qdd3 * sin(q1) * sin(q3) + 24 * l_1 * l_3 * m_6 * qdd3 * sin(q1) * sin(q3) + \
#         12 * l_1 * l_4 * m_5 * qdd4 * sin(q1) * sin(q4) + 24 * l_1 * l_4 * m_6 * qdd4 * sin(q1) * sin(q4) - \
#         12 * l_1 * l_5 * m_7 * qdd5 * sin(q1) * sin(q5)
#
#     M2 = \
#         12 * l_2 * l_3 * m_4 * qdd3 * cos(q2) * cos(q3) - 6 * l_2 ** 2 * m_3 * qdd2 * cos(q2) ** 2 - \
#         24 * l_2 ** 2 * m_4 * qdd2 * cos(q2) ** 2 - 24 * l_2 ** 2 * m_5 * qdd2 * cos(q2) ** 2 - \
#         24 * l_2 ** 2 * m_6 * qdd2 * cos(q2) ** 2 - 24 * l_2 ** 2 * m_7 * qdd2 * cos(q2) ** 2 - \
#         6 * l_2 ** 2 * m_3 * qdd2 * sin(q2) ** 2 - 24 * l_2 ** 2 * m_4 * qdd2 * sin(q2) ** 2 - \
#         24 * l_2 ** 2 * m_5 * qdd2 * sin(q2) ** 2 - 24 * l_2 ** 2 * m_6 * qdd2 * sin(q2) ** 2 - \
#         24 * l_2 ** 2 * m_7 * qdd2 * sin(q2) ** 2 - 12 * l_1 * l_2 * m_3 * qdd1 * cos(q1) * cos(q2) - \
#         24 * l_1 * l_2 * m_4 * qdd1 * cos(q1) * cos(q2) - 24 * l_1 * l_2 * m_5 * qdd1 * cos(q1) * cos(q2) - \
#         24 * l_1 * l_2 * m_6 * qdd1 * cos(q1) * cos(q2) - 24 * l_1 * l_2 * m_7 * qdd1 * cos(q1) * cos(q2) - \
#         2 * l_3 ** 2 * m_3 * qdd2 + 24 * l_2 * l_3 * m_5 * qdd3 * cos(q2) * cos(q3) + \
#         24 * l_2 * l_3 * m_6 * qdd3 * cos(q2) * cos(q3) + 12 * l_2 * l_4 * m_5 * qdd4 * cos(q2) * cos(q4) + \
#         24 * l_2 * l_4 * m_6 * qdd4 * cos(q2) * cos(q4) - 12 * l_2 * l_5 * m_7 * qdd5 * cos(q2) * cos(q5) - \
#         12 * l_1 * l_2 * m_3 * qdd1 * sin(q1) * sin(q2) - 24 * l_1 * l_2 * m_4 * qdd1 * sin(q1) * sin(q2) - \
#         24 * l_1 * l_2 * m_5 * qdd1 * sin(q1) * sin(q2) - 24 * l_1 * l_2 * m_6 * qdd1 * sin(q1) * sin(q2) - \
#         24 * l_1 * l_2 * m_7 * qdd1 * sin(q1) * sin(q2) + 12 * l_2 * l_3 * m_4 * qdd3 * sin(q2) * sin(q3) + \
#         24 * l_2 * l_3 * m_5 * qdd3 * sin(q2) * sin(q3) + 24 * l_2 * l_3 * m_6 * qdd3 * sin(q2) * sin(q3) + \
#         12 * l_2 * l_4 * m_5 * qdd4 * sin(q2) * sin(q4) + 24 * l_2 * l_4 * m_6 * qdd4 * sin(q2) * sin(q4) - \
#         12 * l_2 * l_5 * m_7 * qdd5 * sin(q2) * sin(q5)
#
#     M3 = \
#         12 * l_1 * l_3 * m_4 * qdd1 * cos(q1) * cos(q3) - 6 * l_3 ** 2 * m_4 * qdd3 * cos(q3) ** 2 - \
#         24 * l_3 ** 2 * m_5 * qdd3 * cos(q3) ** 2 - 24 * l_3 ** 2 * m_6 * qdd3 * cos(q3) ** 2 - \
#         6 * l_3 ** 2 * m_4 * qdd3 * sin(q3) ** 2 - 24 * l_3 ** 2 * m_5 * qdd3 * sin(q3) ** 2 - \
#         24 * l_3 ** 2 * m_6 * qdd3 * sin(q3) ** 2 - 2 * l_4 ** 2 * m_4 * qdd3 + \
#         24 * l_1 * l_3 * m_5 * qdd1 * cos(q1) * cos(q3) + \
#         24 * l_1 * l_3 * m_6 * qdd1 * cos(q1) * cos(q3) + 12 * l_2 * l_3 * m_4 * qdd2 * cos(q2) * cos(q3) + \
#         24 * l_2 * l_3 * m_5 * qdd2 * cos(q2) * cos(q3) + 24 * l_2 * l_3 * m_6 * qdd2 * cos(q2) * cos(q3) - \
#         12 * l_3 * l_4 * m_5 * qdd4 * cos(q3) * cos(q4) - 24 * l_3 * l_4 * m_6 * qdd4 * cos(q3) * cos(q4) + \
#         12 * l_1 * l_3 * m_4 * qdd1 * sin(q1) * sin(q3) + 24 * l_1 * l_3 * m_5 * qdd1 * sin(q1) * sin(q3) + \
#         24 * l_1 * l_3 * m_6 * qdd1 * sin(q1) * sin(q3) + 12 * l_2 * l_3 * m_4 * qdd2 * sin(q2) * sin(q3) + \
#         24 * l_2 * l_3 * m_5 * qdd2 * sin(q2) * sin(q3) + 24 * l_2 * l_3 * m_6 * qdd2 * sin(q2) * sin(q3) - \
#         12 * l_3 * l_4 * m_5 * qdd4 * sin(q3) * sin(q4) - 24 * l_3 * l_4 * m_6 * qdd4 * sin(q3) * sin(q4)
#     M4 = \
#         12 * l_1 * l_4 * m_5 * qdd1 * cos(q1) * cos(q4) - 6 * l_4 ** 2 * m_5 * qdd4 * cos(q4) ** 2 - \
#         24 * l_4 ** 2 * m_6 * qdd4 * cos(q4) ** 2 - 6 * l_4 ** 2 * m_5 * qdd4 * sin(q4) ** 2 - \
#         24 * l_4 ** 2 * m_6 * qdd4 * sin(q4) ** 2 - 2 * l_5 ** 2 * m_5 * qdd4 + \
#         24 * l_1 * l_4 * m_6 * qdd1 * cos(q1) * cos(q4) + 12 * l_2 * l_4 * m_5 * qdd2 * cos(q2) * cos(q4) + \
#         24 * l_2 * l_4 * m_6 * qdd2 * cos(q2) * cos(q4) - 12 * l_3 * l_4 * m_5 * qdd3 * cos(q3) * cos(q4) - \
#         24 * l_3 * l_4 * m_6 * qdd3 * cos(q3) * cos(q4) + 12 * l_1 * l_4 * m_5 * qdd1 * sin(q1) * sin(q4) + \
#         24 * l_1 * l_4 * m_6 * qdd1 * sin(q1) * sin(q4) + 12 * l_2 * l_4 * m_5 * qdd2 * sin(q2) * sin(q4) + \
#         24 * l_2 * l_4 * m_6 * qdd2 * sin(q2) * sin(q4) - 12 * l_3 * l_4 * m_5 * qdd3 * sin(q3) * sin(q4) - \
#         24 * l_3 * l_4 * m_6 * qdd3 * sin(q3) * sin(q4)
#
#
#     M5 = \
#         -2 * l_6 ** 2 * m_6 * qdd5 - 6 * l_5 ** 2 * m_7 * qdd5 * cos(q5) ** 2 -\
#         6 * l_5 ** 2 * m_7 * qdd5 * sin(q5) ** 2 - 12 * l_1 * l_5 * m_7 * qdd1 * cos(q1) * cos(q5) - \
#         12 * l_2 * l_5 * m_7 * qdd2 * cos(q2) * cos(q5) - 12 * l_1 * l_5 * m_7 * qdd1 * sin(q1) * sin(q5) - \
#         12 * l_2 * l_5 * m_7 * qdd2 * sin(q2) * sin(q5)
#
#
#     M6 = -2 * l_7 ** 2 * m_7 * qdd6


def getC(sub):

    lengths = sub._link_lengths
    masses = sub._link_masses
    l_1 = lengths[0]
    l_2 = lengths[1]
    l_3 = lengths[2]
    l_4 = lengths[3]
    l_5 = lengths[4]
    l_6 = lengths[5]
    l_7 = lengths[6]
    m_1 = masses[0]
    m_2 = masses[1]
    m_3 = masses[2]
    m_4 = masses[3]
    m_5 = masses[4]
    m_6 = masses[5]
    m_7 = masses[6]

    C1 = \
        12 * l_1 * l_2 * m_3 * qd2 ** 2 * cos(q1) * sin(q2) - 12 * l_1 * l_2 * m_3 * qd2 ** 2 * cos(q2) * sin(q1) + \
        24 * l_1 * l_2 * m_4 * qd2 ** 2 * cos(q1) * sin(q2) - 24 * l_1 * l_2 * m_4 * qd2 ** 2 * cos(q2) * sin(q1) + \
        24 * l_1 * l_2 * m_5 * qd2 ** 2 * cos(q1) * sin(q2) - 24 * l_1 * l_2 * m_5 * qd2 ** 2 * cos(q2) * sin(q1) + \
        24 * l_1 * l_2 * m_6 * qd2 ** 2 * cos(q1) * sin(q2) - 24 * l_1 * l_2 * m_6 * qd2 ** 2 * cos(q2) * sin(q1) + \
        24 * l_1 * l_2 * m_7 * qd2 ** 2 * cos(q1) * sin(q2) - 24 * l_1 * l_2 * m_7 * qd2 ** 2 * cos(q2) * sin(q1) - \
        12 * l_1 * l_3 * m_4 * qd3 ** 2 * cos(q1) * sin(q3) + 12 * l_1 * l_3 * m_4 * qd3 ** 2 * cos(q3) * sin(q1) - \
        24 * l_1 * l_3 * m_5 * qd3 ** 2 * cos(q1) * sin(q3) + 24 * l_1 * l_3 * m_5 * qd3 ** 2 * cos(q3) * sin(q1) - \
        24 * l_1 * l_3 * m_6 * qd3 ** 2 * cos(q1) * sin(q3) + 24 * l_1 * l_3 * m_6 * qd3 ** 2 * cos(q3) * sin(q1) - \
        12 * l_1 * l_4 * m_5 * qd4 ** 2 * cos(q1) * sin(q4) + 12 * l_1 * l_4 * m_5 * qd4 ** 2 * cos(q4) * sin(q1) - \
        24 * l_1 * l_4 * m_6 * qd4 ** 2 * cos(q1) * sin(q4) + 24 * l_1 * l_4 * m_6 * qd4 ** 2 * cos(q4) * sin(q1) + \
        12 * l_1 * l_5 * m_7 * qd5 ** 2 * cos(q1) * sin(q5) - 12 * l_1 * l_5 * m_7 * qd5 ** 2 * cos(q5) * sin(q1)

    C2 = \
        12 * l_1 * l_2 * m_3 * qd1 ** 2 * cos(q2) * sin(q1) - 12 * l_1 * l_2 * m_3 * qd1 ** 2 * cos(q1) * sin(q2) - \
        24 * l_1 * l_2 * m_4 * qd1 ** 2 * cos(q1) * sin(q2) + 24 * l_1 * l_2 * m_4 * qd1 ** 2 * cos(q2) * sin(q1) - \
        24 * l_1 * l_2 * m_5 * qd1 ** 2 * cos(q1) * sin(q2) + 24 * l_1 * l_2 * m_5 * qd1 ** 2 * cos(q2) * sin(q1) - \
        24 * l_1 * l_2 * m_6 * qd1 ** 2 * cos(q1) * sin(q2) + 24 * l_1 * l_2 * m_6 * qd1 ** 2 * cos(q2) * sin(q1) - \
        24 * l_1 * l_2 * m_7 * qd1 ** 2 * cos(q1) * sin(q2) + 24 * l_1 * l_2 * m_7 * qd1 ** 2 * cos(q2) * sin(q1) - \
        12 * l_2 * l_3 * m_4 * qd3 ** 2 * cos(q2) * sin(q3) + 12 * l_2 * l_3 * m_4 * qd3 ** 2 * cos(q3) * sin(q2) - \
        24 * l_2 * l_3 * m_5 * qd3 ** 2 * cos(q2) * sin(q3) + 24 * l_2 * l_3 * m_5 * qd3 ** 2 * cos(q3) * sin(q2) - \
        24 * l_2 * l_3 * m_6 * qd3 ** 2 * cos(q2) * sin(q3) + 24 * l_2 * l_3 * m_6 * qd3 ** 2 * cos(q3) * sin(q2) - \
        12 * l_2 * l_4 * m_5 * qd4 ** 2 * cos(q2) * sin(q4) + 12 * l_2 * l_4 * m_5 * qd4 ** 2 * cos(q4) * sin(q2) - \
        24 * l_2 * l_4 * m_6 * qd4 ** 2 * cos(q2) * sin(q4) + 24 * l_2 * l_4 * m_6 * qd4 ** 2 * cos(q4) * sin(q2) + \
        12 * l_2 * l_5 * m_7 * qd5 ** 2 * cos(q2) * sin(q5) - 12 * l_2 * l_5 * m_7 * qd5 ** 2 * cos(q5) * sin(q2)

    C3 = \
        12 * l_1 * l_3 * m_4 * qd1 ** 2 * cos(q1) * sin(q3) - 12 * l_1 * l_3 * m_4 * qd1 ** 2 * cos(q3) * sin(q1) + \
        24 * l_1 * l_3 * m_5 * qd1 ** 2 * cos(q1) * sin(q3) - 24 * l_1 * l_3 * m_5 * qd1 ** 2 * cos(q3) * sin(q1) + \
        24 * l_1 * l_3 * m_6 * qd1 ** 2 * cos(q1) * sin(q3) - 24 * l_1 * l_3 * m_6 * qd1 ** 2 * cos(q3) * sin(q1) + \
        12 * l_2 * l_3 * m_4 * qd2 ** 2 * cos(q2) * sin(q3) - 12 * l_2 * l_3 * m_4 * qd2 ** 2 * cos(q3) * sin(q2) + \
        24 * l_2 * l_3 * m_5 * qd2 ** 2 * cos(q2) * sin(q3) - 24 * l_2 * l_3 * m_5 * qd2 ** 2 * cos(q3) * sin(q2) + \
        24 * l_2 * l_3 * m_6 * qd2 ** 2 * cos(q2) * sin(q3) - 24 * l_2 * l_3 * m_6 * qd2 ** 2 * cos(q3) * sin(q2) + \
        12 * l_3 * l_4 * m_5 * qd4 ** 2 * cos(q3) * sin(q4) - 12 * l_3 * l_4 * m_5 * qd4 ** 2 * cos(q4) * sin(q3) + \
        24 * l_3 * l_4 * m_6 * qd4 ** 2 * cos(q3) * sin(q4) - 24 * l_3 * l_4 * m_6 * qd4 ** 2 * cos(q4) * sin(q3)


    C4 = \
        12 * l_1 * l_4 * m_5 * qd1 ** 2 * cos(q1) * sin(q4) - 12 * l_1 * l_4 * m_5 * qd1 ** 2 * cos(q4) * sin(q1) + \
        24 * l_1 * l_4 * m_6 * qd1 ** 2 * cos(q1) * sin(q4) - 24 * l_1 * l_4 * m_6 * qd1 ** 2 * cos(q4) * sin(q1) + \
        12 * l_2 * l_4 * m_5 * qd2 ** 2 * cos(q2) * sin(q4) - 12 * l_2 * l_4 * m_5 * qd2 ** 2 * cos(q4) * sin(q2) + \
        24 * l_2 * l_4 * m_6 * qd2 ** 2 * cos(q2) * sin(q4) - 24 * l_2 * l_4 * m_6 * qd2 ** 2 * cos(q4) * sin(q2) - \
        12 * l_3 * l_4 * m_5 * qd3 ** 2 * cos(q3) * sin(q4) + 12 * l_3 * l_4 * m_5 * qd3 ** 2 * cos(q4) * sin(q3) - \
        24 * l_3 * l_4 * m_6 * qd3 ** 2 * cos(q3) * sin(q4) + 24 * l_3 * l_4 * m_6 * qd3 ** 2 * cos(q4) * sin(q3)


    C5 = \
        12 * l_1 * l_5 * m_7 * qd1 ** 2 * cos(q5) * sin(q1) - 12 * l_1 * l_5 * m_7 * qd1 ** 2 * cos(q1) * sin(q5) - \
        12 * l_2 * l_5 * m_7 * qd2 ** 2 * cos(q2) * sin(q5) + 12 * l_2 * l_5 * m_7 * qd2 ** 2 * cos(q5) * sin(q2)


    C6 = 0

    C = np.matrix([C1, C2, C3, C4, C5, C6])
    return C

def getG(sub):

    lengths = sub._link_lengths
    masses = sub._link_masses
    l_1 = lengths[0]
    l_2 = lengths[1]
    l_3 = lengths[2]
    l_4 = lengths[3]
    l_5 = lengths[4]
    l_6 = lengths[5]
    l_7 = lengths[6]
    m_1 = masses[0]
    m_2 = masses[1]
    m_3 = masses[2]
    m_4 = masses[3]
    m_5 = masses[4]
    m_6 = masses[5]

    G1 =  10 * l_1 * cos(q1) + 10 * l_1 * sin(q1)
    G2 =  8 * l_2 * cos(q2) + 8 * l_2 * sin(q2)
    G3 = -4 * l_3 * cos(q3) - 4 * l_3 * sin(q3)
    G4 = - 2 * l_4 * cos(q4) - 2 * l_4 * sin(q4)
    G5 = 2 * l_5 * cos(q5) + 2 * l_5 * sin(q5)
    G6 = 0
    G = np.matrix([G1, G2, G3, G4, G5, G6])
    return G



