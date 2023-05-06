import numpy as np
import matplotlib.pyplot as plt




class Suspension2DMechanism:
    def __init__(self, l1: float, l2: float, l3: float, w: float, h: float, phi: float = np.pi/2):
        self.l = np.array([l1, l2, l3])
        self.w = w
        self.h = h

        self.phi = phi

    def forward_kinematics(self, q: np.ndarray):
        # Upper mechanism
        A = np.array([0, 0])
        B = self.l[1] * np.array([np.cos(q[0]), np.sin(q[0])])
        E = np.array([self.w, 0])
        D = E + self.l[1] * np.array([np.cos(q[1]), np.sin(q[1])])

        # Lower mechanism
        r = D - B
        alpha = np.arctan2(r[1], r[0])

        r_norm = np.linalg.norm(r)
        c_gamma = (r_norm**2 - 2*self.l[2]**2) / (2*self.l[2]**2)
        gamma = np.arctan2(np.sqrt(1 - c_gamma**2), c_gamma)

        beta = np.arccos(r_norm/(2*self.l[2]))
        q3 = alpha - beta

        C = B + self.l[2] * np.array([np.cos(q3), np.sin(q3)])

        return np.linalg.norm(C - [self.w/2, self.h])



    def inverse_kinematics(self, L: float):
        pass
        
    def get_points(self, q: np.ndarray):
        # Upper mechanism
        A = np.array([0, 0])
        B = self.l[1] * np.array([np.cos(q[0]), np.sin(q[0])])
        E = np.array([self.w, 0])
        D = E + self.l[1] * np.array([np.cos(q[1]), np.sin(q[1])])

        # Lower mechanism
        r = D - B
        alpha = np.arctan2(r[1], r[0])

        r_norm = np.linalg.norm(r)
        c_gamma = (r_norm**2 - 2*self.l[2]**2) / (2*self.l[2]**2)
        gamma = np.arctan2(np.sqrt(1 - c_gamma**2), c_gamma)

        beta = np.arccos(r_norm/(2*self.l[2]))
        q3 = alpha - beta

        C = B + self.l[2] * np.array([np.cos(q3), np.sin(q3)])

        # 4-bar linkages    
        F = E + self.l[0] * np.array([np.cos(self.phi+q[1]), np.sin(self.phi+q[1])])
        G = F + np.array([0, self.h])
        H = E + np.array([0, self.h])

        I = A + np.array([0, self.h])
        J = I + self.l[0] * np.array([np.cos(-self.phi+q[0]), np.sin(-self.phi+q[0])])
        K = J + np.array([0, -self.h])

        return np.array([A, B, C, D, E, F, G, H, I, J, K])


    def plot(self, q: np.ndarray):
        points = self.get_points(q)
        points = np.vstack((points, points[0, :]))

        L = self.forward_kinematics(q)

        plt.figure()
        plt.plot(points[:, 0], points[:, 1], 'ro-')
        plt.plot([points[2, 0], self.w/2], [points[2, 1], self.h], 'bo-')
        plt.axis('equal')
        plt.title(str(L) + ' m')
        plt.grid()
        plt.show()



if __name__ == "__main__":
    m = Suspension2DMechanism(0.1, 0.02, 0.08, 0.165, 0.03)

    m.plot(np.array([-np.pi/6, -5*np.pi/6]))




