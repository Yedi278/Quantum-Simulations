import numpy as np
import matplotlib.pyplot as plt

class qubit:

    def __init__(self, fig, ax:plt.Axes, theta:float=0, phi:float=0, color='k'):
        self.fig =  fig
        self.ax = ax
        self.theta = theta
        self.phi = phi
        self.color = color
    
    def draw_bloch_sphere(self):
        # Draw Bloch sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))
        
        self.ax.plot_surface(x, y, z, color='b', alpha=0.1, rstride=4, cstride=4)
        
        # draw axes and labels
        size_ = 1.5
        self.ax.set_xlim(-size_, size_)
        self.ax.set_ylim(-size_, size_)
        self.ax.set_zlim(-size_, size_)
        self.ax.quiver(0, 0, 0, size_, 0, 0, color='r', alpha=0.4, arrow_length_ratio=0.1, linestyle='dashed')
        self.ax.quiver(0, 0, 0, 0, size_, 0, color='g', alpha=0.4, arrow_length_ratio=0.1, linestyle='dashed')
        self.ax.quiver(0, 0, 0, 0, 0, size_, color='b', alpha=0.4, arrow_length_ratio=0.1, linestyle='dashed')

        # add labels on |0> and |1> states
        self.ax.text(0, 0, -size_+0.1, '|1>', color='k', alpha=0.5, fontsize=10, ha='center')
        self.ax.text(0, 0, size_+0.1, '|0>', color='k', alpha=0.5, fontsize=10, ha='center')
        # add labels on |+> and |-> states
        self.ax.text(size_+0.1, 0, 0, '|+>', color='k', alpha=0.5, fontsize=10, ha='center')
        self.ax.text(-size_+0.1, 0, 0, '|->', color='k', alpha=0.5, fontsize=10, ha='center')

        self.fig.canvas.draw()

    def draw_projections(self, x, y, z):
        # Draw projections
        self.ax.plot([x, x], [y, 0], [0, 0], color=self.color, alpha=0.3, linestyle='dashed')
        self.ax.plot([x, 0], [y, y], [0, 0], color=self.color, alpha=0.3, linestyle='dashed')

        self.ax.plot([x, x], [y, y], [z, 0], color=self.color, alpha=0.3, linestyle='dashed')

        # self.fig.canvas.draw()

    def set_state(self, theta:float, phi:float):
        self.theta = theta
        self.phi = phi

    def get_psi(self)-> np.array:
        return np.array([np.cos(self.theta/2), np.exp(1j*self.phi) * np.sin(self.theta/2)])
        
    def draw_state(self, show_projections:bool=True):
    
        # Draw qubit state
        x = np.sin(self.theta) * np.cos(self.phi)
        y = np.sin(self.theta) * np.sin(self.phi)
        z = np.cos(self.theta)

        # Draw projections
        if show_projections:
            self.draw_projections(x, y, z)

        self.ax.quiver(0, 0, 0, x, y, z, color=self.color, arrow_length_ratio=0.1)
        
        r = np.sqrt(x**2 + y**2 + z**2)
        alpha = np.arccos(z/r)

        x = r/2 * np.sin(alpha/2) * np.cos(self.phi)
        y = r/2 * np.sin(alpha/2) * np.sin(self.phi)
        z = r/2 * np.cos(alpha/2)

        # add labels on |psi> state
        self.ax.text(x+0.3, y+0.3, z+0.3, '$|\psi>$', color=self.color, fontsize=10, ha='center')

        self.fig.canvas.draw()


if __name__ == '__main__':
    from gates import XGate

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_aspect('equal')
    ax.axis('off')

    q = qubit(fig, ax)
    
    q.draw_bloch_sphere()
    q.set_state(np.pi/4,0)
    
    XGate(q)

    q.draw_state()
    
    plt.show()