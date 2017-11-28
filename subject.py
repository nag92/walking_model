import numpy as np

class subject():

    def __init__(self,mass=64,height=1.7):

        self._total_mass = mass
        self._height = height
        l,r, I = self.calc_links()
        self._centriod = r
        self._link_lengths = l
        self._I = I
        self._link_masses = self.calc_link_mass()
        self._q = np.array([0,0,0,0,0])
        self._qd = []
        self._qdd = []
        self._tau = []

    def calc_link_mass(self):
        """
        add real EQ
        :return:
        """
        return np.array([5,5,5,5,5])


    def calc_links(self):
        """

        :return:
        """
        l = np.array([ 10,10,10,10,10 ])
        I = np.array([ 10,10,10,10,10 ])
        r = 0.5*l
        return  l,r, I

        pass


    def get_params(self):
        return (self._link_masses,self._I,self._link_lengths,self._centriod)