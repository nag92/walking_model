

import numpy as np
import subject

M = np.matrix([[1, 0, 0, 0, 0],
               [-1, 1, 0, 0, 0],
               [0, -1, 1, 0, 0],
               [0, 0, -1, 1, 0],
               [0, 0, 0, -1, 1]])
invM = np.linalg.inv(M)
invMT = invM.transpose()


def euler_lagrange(subject):
    """

    :param robot:
    :return:
    """
    g = 9.81
    masses,inertias,lengths,centriods = subject.get_params()
    q = subject._q
    qd = subject._qd
    qdd = subject._qdd
    D = np.zeros(shape=(5, 5))
    H = np.zeros(shape=(5, 5))
    G = np.zeros(shape=(5, 1))
    p = np.zeros(shape=(5, 5))

    M = np.matrix([[1, 0, 0, 0, 0],
                   [-1, 1, 0, 0, 0],
                   [0, -1, 1, 0, 0],
                   [0, 0, -1, 1, 0],
                   [0, 0, 0, -1, 1]])
    invM = np.linalg(M)
    invMT = invM.transpose()

    for i in xrange(5):

        a_i = int(not (i == 2))
        G[i] = (m[i] * centriods[i] * g + a_i*sum(masses[i+1:])*lengths[i]*g)*np.sin(q[i])

        for j in xrange(5):


            a_j = int(not (j == 2))

            if i == j:
                m = sum(masses[i+1:])
                p[i][j] = inertias[i] + masses[i]*centriods[i]**2 +a_i*m*lengths[i]**2
            elif j > i:
                m = sum(masses[j + 1:])
                p[i][j] = a_i*masses[j]*centriods[j]*lengths[i]+ \
                    a_i*a_j*m*lengths[i]*lengths[j]
            else:
                p[i][j] = p[j][i]

            D[i][j] = p[i][j] * np.cos(q[i] - q[j])
            H[i][j] = p[i][j] * np.sin(q[i] - q[j])*qd[j]

    D_q = invMT*D*invM
    H_q = invMT*H*invM
    G_q = invMT*G

    return D_q*qdd + H_q*qd + G_q



    

def jacobian(sub):
    """

    :param subject:
    :return:
    """

    masses,inertias,lengths,centriods = sub.get_params()
    q = sub._q
    qd = sub._qd
    qdd = sub._qdd

    j = np.zeros(shape=(2, 5))

    for i in xrange(5):

        j[0][i] =  lengths[0] * np.cos(q[i])
        j[1][i] = -lengths[0] * np.sin(q[i])

    j[0][2] = 0
    j[1][2] = 0

    return j*invM


sub = subject.subject()
print jacobian(sub)


def impact(sub):
    """

    :param sub:
    :return:
    """
    m, I, l, d = sub.get_params()
    q = sub._q
    qd = sub._qd
    W = np.zeros(shape=(5, 5))

    j = jacobian(sub)
    j_T = j.transpose()

    for i in xrange(5):
        a_i = int(not (i == 2))
        for j in xrange(5):
            a_j = int(not (j == 2))
            if j == i:
                W[i][j] = I[i] - m[i] * d * ( a_i *  l[i] - d[i] )
            elif j < i:
                W[i][j] = (a_i * m[j] * d[j] *l[i] + a_j * m[i] * l[j] ( a_i *l[i] - d[i] ) \
                          + a_i*a_j*l[i]*l[j]*sum(m[j+1:]))*np.cos(q[i] - q[j])
            else:
                W[i][j] = 0






