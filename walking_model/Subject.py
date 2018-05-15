import numpy as np
import dynamics
from walking_model.common import *


class Subject():
    """
        This class models the subject under test.
        Its kinematics and dynamics are calculated here
    """

    def __init__(self, mass=64, height=1.7):
        """

        :param mass: mass of the subject
        :param height: height of the subject
        """
        self._total_mass = mass
        self._height = height
        self._link_lengths = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        self._link_masses = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)

        self.q = np.array([[0], [0], [0], [0], [0], [0]], dtype=float)
        self.qd = np.array([0, 0, 0, 0, 0, 0], dtype=float)
        self.qdd = np.array([0, 0, 0, 0, 0, 0], dtype=float)

        self.q_old = self.q
        self.qd_old = self.q

        self.tau = np.array([0, 0, 0, 0, 0, 0], dtype=float)

        self.fixed = np.matrix([[0], [0]])
        self.single_phase = 0
        self.right = True
        self.set_links()
        self.switch_gate()
        self.joints = dynamics.FK(self)
        self.old_y = 0
        self.switch = np.array([[0, 0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0],
                                [1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 0, 1]])

    def update(self, q):
        self.q = np.asarray([[i] for i in q])

        self.joints = dynamics.FK(self)
        # print(self.fixed)
        self.check_phase()
        self.switch_gate()
        self.q = self.switch.dot(self.q)
        self.joints = dynamics.FK(self)

        # compute torque

        self.get_torques()

        self.q_old = self.q
        self.qd_old = self.qd

    def get_torques(self):
        mass_matrix = dynamics.get_mass_matrix(self)
        coriolis_matrix = dynamics.get_coriolis_matrix(self)
        gravity_matrix = dynamics.get_gravity_matrix(self)

        self.qd = self.q_old - self.q
        self.qdd = self.qd_old - self.qd

        self.tau = mass_matrix * self.qdd + coriolis_matrix + gravity_matrix.T

    def check_phase(self):
        points = self.joints
        x, y = zip(*points)

        x_5 = x[4]
        y_5 = y[4]

        if not self.right:
            y_5 *= -1

        # Zero crossing detector
        if (y_5 <= 0.0) and (self.old_y >= 0.0):

            increment_gait_count()

            logging.warn(WARNING + "PHASE CHANGED" + ENDC)
            logging.info("Double support")

            self.single_phase = False

            self.fixed = np.matrix([[x_5],
                                    [0]])

            # toggle front and back leg
            self.right = not self.right

        else:
            logging.info("Single support")
            logging.info("Right leg forward:{}".format(
                OKGREEN + "{}".format(self.right) if self.right else FAIL + "{}".format(self.right)) + ENDC)
            self.single_phase = True

        self.old_y = y_5

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

        # shins
        self._link_lengths[1] = 0.246 * self._height
        self._link_lengths[5] = 0.246 * self._height

        # thighs
        self._link_lengths[2] = 0.245 * self._height
        self._link_lengths[4] = 0.245 * self._height

        # trunk
        self._link_lengths[6] = 0.245 * self._height

        self._link_lengths[0] = 0.152 * self._height
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

        # trunk
        self._link_masses[6] = 0.245 * self._height
