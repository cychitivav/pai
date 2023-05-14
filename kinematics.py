import numpy as np
import matplotlib.pyplot as plt




class Suspension2DMechanism:
    def __init__(self, l1: float, l2: float, l3: float, w: float, h: float, phi: float = np.pi/2):
        self.l = np.array([l1, l2, l3])
        self.w = w
        self.h = h

        self.phi = phi

    def forward_kinematics(self, q: np.ndarray):
        return np.linalg.norm(self.get_points(q)[2, :] - np.array([0, self.h]))

    def inverse_kinematics(self, L: float):
        pass
        
    def get_points(self, q: np.ndarray):
        # Upper mechanism
        A = np.array([-self.w/2, 0])
        B = A + self.l[1] * np.array([np.cos(q[0]), np.sin(q[0])])
        E = np.array([self.w/2, 0])
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

        L = 0.125-np.linalg.norm(points[2, :] - np.array([0, self.h]))
        K = 400*(0.453592*9.81) * 0.0254 # N/m
        F = K * L

        plt.plot(points[:, 0], points[:, 1], 'ro-')
        plt.plot([points[0, 0], points[4, 0]], [points[0, 1], points[4, 1]], 'ro-')
        plt.plot([points[2, 0], 0], [points[2, 1], self.h], 'bo-')  
        plt.axis('equal')
        plt.title(str(L) + ' m\n' + str(F) + ' N')
        plt.grid()



if __name__ == "__main__":
    m = Suspension2DMechanism(0.1, 0.02, 0.08, 0.165, 2*0.025)

    for q1 in np.linspace(-np.pi/4, -np.pi/2):
        for q2 in np.linspace(-np.pi/2, -3*np.pi/4):

            plt.figure(1)
            m.plot(np.array([q1, q2]))
            plt.xlim([-0.3, 0.3])
            plt.ylim([-0.1, 0.1])
            plt.pause(0.005)
            plt.clf()





