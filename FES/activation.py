
from math import sin,exp
import numpy as np

def moment_arm(hip,knee,ankle):

    ma = np.zeros((9,3))
    ma[0,0] = 0.00233 * hip ** 2 - 0.00223 * hip - 0.0275
    ma[1,0] = -0.0098 * hip ** 2 - 0.0054 * hip + 0.0413
    ma[2,0] =  -0.020 * hip ** 2 - 0.024 * hip + 0.055
    ma[4,0] = 0.025 * hip ** 2 + 0.41 * hip - 0.040

    ma[2,1]  = -0.0098 * knee ** 2 + 0.021 * knee + 0.028
    ma[3,1]  = -0.008 * knee ** 2 + 0.027 * knee + 0.014
    ma[4,1]  = -0.058 * exp(-2.0 * knee ** 2) * sin(knee) - 0.0284
    ma[5,1]  = -0.07 * exp(-2.0 * knee ** 2) * sin(knee) - 0.0250
    ma[6,1]  = 0.018

    ma[6][2]  = 0.053
    ma[7,2]  = 0.035
    ma[8,2]  = 0.013 * ankle - 0.035
    return ma


def elastic_moments(hip,knee,ankle):
    """
    Calculate the elastic moments
    :param hip:
    :param knee:
    :param ankle:
    :return:
    """

    m_h = exp(2.180 - 0.0160 * ankle - 0.0195 * hip) - exp(-2.1784 + 0.070 * knee + 0.1349 * hip) - 15.24

    m_k = exp(1.0372 + 0.0040 * ankle - 0.0494 * knee - 0.0250 * hip) - exp(-1.1561 - 0.0020 * knee + 0.0030 * hip) + \
          exp(2.5 - 0.25 * knee) + 1.0


    m_a = exp(2.0111 - 0.0833 * ankle - 0.0090) - exp(-9.9250 + 0.2132 * ankle) - 2.970;


    return (m_h, m_k,m_a)