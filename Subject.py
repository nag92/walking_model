import numpy as np
import dynamics

class Subject():

    def __init__(self,mass=64,height=1.7):
        """

        :param mass:
        :param height:
        """
        self._total_mass = mass
        self._height = height
        self._link_lengths = np.array([0,0,0,0,0,0,0],dtype=float)
        self._link_masses = np.array([0,0,0,0,0,0,0],dtype=float)
        self.q = np.array([[0],[0],[0],[0],[0],[0]],dtype=float)
        self.qd = np.array([0,0,0,0,0,0],dtype=float)
        self.tau = np.array([0,0,0,0,0,0],dtype=float)

        self.joints = []
        self.fixed = np.array([[0],[0]])
        self.phase = 0
        self.right = True
        self.set_links()


    def update(self, q):
        self.q = np.asarray([[i] for i in q ])
        self.joints = dynamics.FK(self,self.fixed)

        self.check_phase()
        if  self.right:
            print "hello"
            switch = np.array([ [0, 0, 0, 1, 0 ,0],
                                 [0, 0, 1, 0, 0, 0],
                                 [0, 1, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 1, 0],
                                 [0, 0, 0, 0, 0, 1]])
            print self.q
            self.q = switch.dot(self.q)




    def check_phase(self):
        temp =  self.joints[4][1].tolist()[0][0]
        self.phase = temp < 0.001
        print self.phase

        self.right = (self.right and self.phase)


    def set_links(self):

        # feet
        self._link_lengths[0] = 1#0.152*self._height
        self._link_lengths[5] = 1#0.152 * self._height
        self._link_masses[0] = 0.0143 * self._height
        self._link_masses[5] = 0.0143 * self._height

        # shins
        self._link_lengths[1] = 1#0.246 * self._height
        self._link_lengths[4] = 1#0.246 * self._height
        self._link_masses[1] = 0.0475 * self._height
        self._link_masses[4] = 0.0475 * self._height

        # thighs
        self._link_lengths[2] = 1#0.245 * self._height
        self._link_lengths[3] = 1#0.245 * self._height
        self._link_masses[2] = 0.105 * self._total_mass
        self._link_masses[3] = 0.105 * self._total_mass

        # trunk
        self._link_lengths[6] = 1#0.245 * self._height
        self._link_masses[6] = 0.245 * self._height












