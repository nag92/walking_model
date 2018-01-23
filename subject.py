import numpy as np

class subject():

    def __init__(self,mass=64,height=1.7):
        """

        :param mass:
        :param height:
        """
        self._total_mass = mass
        self._height = height
        self._link_lengths = []
        self._link_masses = []
        self._q = np.array([0,0,0,0,0,0])
        self._qd = []
        self._tau = []


    def set_links(self):

        # feet
        self._link_lengths[0] = 0.152*self._height
        self._link_lengths[5] = 0.152 * self._heightc
        self._link_masses[0] = 0.0143 * self._height
        self._link_masses[5] = 0.0143 * self._height

        # shins
        self._link_lengths[1] = 0.246 * self._height
        self._link_lengths[4] = 0.246 * self._height
        self._link_masses[1] = 0.0475 * self._height
        self._link_masses[4] = 0.0475 * self._height

        # thighs
        self._link_lengths[2] = 0.245 * self._height
        self._link_lengths[3] = 0.245 * self._height
        self._link_masses[2] = 0.105 * self._total_mass
        self._link_masses[3] = 0.105 * self._total_mass

        # trunk
        self._link_lengths[6] = 0.245 * self._height
        self._link_masses[6] = 0.245 * self._height












