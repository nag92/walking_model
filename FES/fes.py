
from math import sin,exp
import numpy as np

def moment_arm(sub):

    theta = sub.q

    hip = theta[0]
    knee = theta[1]
    ankle = theta[2]
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


def elastic_moments(sub):
    """
    Calculate the elastic moments
    :param hip:
    :param knee:
    :param ankle:
    :return:
    """
    theta = sub.q

    hip = theta[0]
    knee = theta[1]
    ankle = theta[2]

    m_h = exp(2.180 - 0.0160 * ankle - 0.0195 * hip) - exp(-2.1784 + 0.070 * knee + 0.1349 * hip) - 15.24

    m_k = exp(1.0372 + 0.0040 * ankle - 0.0494 * knee - 0.0250 * hip) - exp(-1.1561 - 0.0020 * knee + 0.0030 * hip) + \
          exp(2.5 - 0.25 * knee) + 1.0


    m_a = exp(2.0111 - 0.0833 * ankle - 0.0090) - exp(-9.9250 + 0.2132 * ankle) - 2.970;


    return (m_h, m_k,m_a)

def viscous_moments(sub):
    """
    Viscous moments
    :param dh:
    :param dk:
    :param da:
    :return:
    """
    dtheta = sub.qd
    hip   = dtheta[0]
    knee  = dtheta[1]
    ankle = dtheta[2]

    k_a = 0.6
    k_k = 1.0
    k_h = 2.0

    return (k_h*hip,k_k*knee,k_a*ankle)

def norm_l(sub):
    """
    TODO get the real length
    normilized length
    :param theta:
    :return:
    """
    theta = sub.q
    C = [0.165, 0.05, 0.09, 0.18, 0.11, 0.04, 0.06, 0.028, 0.09]
    lopt = [0146, 0.11, 0.121, 0.173, 0.086, 0.086, 0.054, 0.033, 0.099]
    return np.ones(9)

def norm_v(sub):
    """
    normilized velcity

    :param theta:
    :param dtheta:
    :return:
    """
    theta = sub.q
    dtheta = sub.qd
    v  = np.zeros((9,1))
    vm = [0.73, 0.54, 0.48, 0.69, 0.51, 0.48, 0.32, 0.1, 0.36]

    ma = moment_arm(theta)


    for i in xrange(9):

        v[i] = sum(dtheta * ma[i])/vm[i]

    return v

def force_length(sub):

    theta = sub.q
    l = norm_l(theta)
    ep = np.array([0.4,0.5,0.4,0.2,0.4,0.45,0.3,0.5,0.4])

    return np.exp( (l - np.ones(9))/(ep))

def force_velocity(sub):
    theta = sub.q
    dtheta = sub.qd
    v_hat = norm_v(theta,dtheta)
    return 0.54*np.arctan( 5.69*v_hat + 0.51) + 0.754


def muscle_force(activation, sub):

    f_max = 0.45*np.array([1850,2370,2190,400,1000,5200,1600,3600,1100])
    fv = force_velocity(sub)
    fl = force_length(sub)
    return activation*f_max*fv*fl

def activation(pulse, freq):

    d_thr = 122.0
    d_sat = 487.0
    alpha = 0.1
    beta  = 0.6
    k_thr = 0.5
    k_sat = 0.5

    max_d = 999999999

    n1 = (-d_thr) * np.arctan(k_thr * -d_thr) - (-d_sat) * np.arctan(k_sat * -d_sat)
    n2 = (max_d - d_thr) * np.arctan(k_thr * (max_d - d_thr)) - (max_d - d_sat) * np.arctan(k_sat * (max_d - d_sat))

    c1 = 1 / (n2 - n1);
    c2 = -n1 / (n2 - n1);

    a_r = c1 * ((pulse - d_thr) * np.arctan(k_thr * (pulse - d_thr)) -
                (pulse - d_sat) * np.arctan(k_sat * (pulse - d_sat))) + c2

    temp = (alpha * freq) ** 2

    a_f = temp / (1 + temp)
    a_p = a_f * a_r;

    return a_p

def get_torque(sub, pulse, freq=30):

    ma = moment_arm(sub);
    a_p = activation(pulse, freq)
    M_ela = elastic_moments(sub)
    M_vis = viscous_moments(sub)
    M_force = muscle_force(a_p,sub)
    return M_force + M_ela + M_vis


