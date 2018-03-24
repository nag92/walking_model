import numpy as np
import dynamics
from walking_model.logger import * 

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


        self.fixed = np.matrix([[0],[0]])
        self.single_phase = 0
        self.right = True
        self.set_links()
        self.switch_gate()
        self.joints = dynamics.FK(self)
        self.old_y = 0


    def update(self, q):
        self.q = np.asarray([[i] for i in q ])

        self.joints = dynamics.FK(self)
        #print(self.fixed)
        self.check_phase()
        self.switch_gate()
        self.q = self.switch.dot(self.q)
        self.joints = dynamics.FK(self)


    def check_phase(self):

        # points = dynamics.FK(self)
        points = self.joints
        x, y = zip(*points)
        
        print "-"*80
        for idx,pt in enumerate(points):
            # print "points:>>",pt
            logging.info("point_{}: {}".format(idx,pt))
        print "-"*80
        # print "x_5:",x[4],"y_5:",y[4]
        logging.info("x_5:{} | y_5: {}".format(x[4],y[4]))
        print "-"*80
        
        # if not self.right:
        #     x=[x[len(x)-1-i] for i in range(len(x))]
        #     y=[y[len(y)-1-i] for i in range(len(y))]

        # y_5  = y[4]
        # x_5  = x[4]

        x_5  = x[4]
        y_5  = y[4]
        # x_0  = x[0]

        if not  self.right:
            y_5*=-1

        # print "sub"
        # print "x", x
        # print "y", y

        # Zero crossing detector
        if ( (y_5 <= 0.0 and self.old_y >= 0.0)  ):
            # print "#"*80
            # print "PHASE CHANGED"
            logging.warn("PHASE CHANGED")
            logging.info("double support")
            # print "#"*80
            # print "double"
            self.single_phase = False

            self.fixed = np.matrix([[x_5],
                                    [0]])
            
            # toggle front and back leg
            self.right = not self.right

        else:
            # print "single"
            # print "Right first:",self.right
            logging.info("Single support")
            logging.info("Right first:{}".format(self.right))
            self.single_phase = True

        # if not self.right:
        #     self.switch = np.array([[0, 0, 0, 1, 0, 0],
        #                             [0, 0, 1, 0, 0, 0],
        #                             [0, 1, 0, 0, 0, 0],
        #                             [1, 0, 0, 0, 0, 0],
        #                             [0, 0, 0, 0, 1, 0],
        #                             [0, 0, 0, 0, 0, 1]])
        # else:
        #     self.switch = np.array([[1, 0, 0, 0, 0, 0],
        #                             [0, 1, 0, 0, 0, 0],
        #                             [0, 0, 1, 0, 0, 0],
        #                             [0, 0, 0, 1, 0, 0],
        #                             [0, 0, 0, 0, 1, 0],
        #                             [0, 0, 0, 0, 0, 1]])
        # self.switch_gate()

        self.old_y = y_5


        # print x
        # self.phase = (y < 0 and self.old_y > y) and x > x2
        # print self.phase
        # if self.phase:
        #
        #     self.right = not self.right
        #     self.fixed = np.matrix( [ [self.joints[4][0].tolist()[0][0]],[0]])
        #
        # self.old_y = y

    def switch_gate(self):
        if not self.right:
            self.switch = np.array([[0, 0, 0, 1, 0, 0],
                                    [0, 0, 1, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 1, 0],
                                    [0, 0, 0, 0, 0, 1]])
        else:
            self.switch = np.array([[1, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0],
                                    [0, 0, 1, 0, 0, 0],
                                    [0, 0, 0, 1, 0, 0],
                                    [0, 0, 0, 0, 1, 0],
                                    [0, 0, 0, 0, 0, 1]])


    def set_links(self):


        # LINK LENGTHS

        # Fee6        
        # self._link_lengths

        # shins
        self._link_lengths[1] = 0.246 * self._height
        self._link_lengths[5] = 0.246 * self._height
        
        

        # thighs
        self._link_lengths[2] = 0.245 * self._height
        self._link_lengths[4] = 0.245 * self._height
        
        
        # trunk
        self._link_lengths[6] = 0.245 * self._height

        self._link_lengths[0] = 0.152*self._height
        self._link_lengths[3] = 0.152 * self._height


        # LINK MASS

        # feet
        self._link_masses[0] = 0.0143 * self._total_mass
        self._link_masses[5] = 0.0143 * self._total_mass

        # shin
        self._link_masses[1] = 0.0475 * self._total_mass
        self._link_masses[4] = 0.0475 * self._total_mass

        # thigh
        self._link_masses[2] = 0.105 * self._total_mass
        self._link_masses[3] = 0.105 * self._total_mass

        #trunk
        self._link_masses[6] = 0.245 * self._height





