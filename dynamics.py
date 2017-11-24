

import numpy as np



def euler_lagrange(subject):
    """

    :param robot:
    :return:
    """
    g = 9.81
    masses,inertias,lengths,centriods = subject.get_params()
    q = subject._q
    qd = subject._qd
    D = np.zeros(shape=(5, 5))
    H = np.zeros(shape=(5, 5))
    G = np.zeros(shape=(5, 1))
    p = np.zeros(shape=(5, 5))

    for i in xrange(5):

        a_i = int(not (i == 2))
        G[i] = m[i] * centriods[i] * g + a_i*sum(masses[i+1:])*lengths[i]*g

        for j in xrange(5):


            a_j = int(not (i == 2))

            if i == j:
                m = sum(masses[i+1:])
                p[i][j] = inertias[i] + masses[i]*centriods[i]**2 +a_i*m*lengths[i]**2
            elif j > i:
                m = sum(masses[j + 1:])
                p[i][j] = a_i*masses[j]*centriods[j]*lengths[i]+ \
                    a_i*a_j*m*lengths[i]*lengths[j]
            else:
                p[i][j] = p[j][i]

            G[i][j] = p[i][j] * np.cos(q[i] - q[j])
            H[i][j] = p[i][j] * np.sin(q[i] - q[j])*qd[j]



    



