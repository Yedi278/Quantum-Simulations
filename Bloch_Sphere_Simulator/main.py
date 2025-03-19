import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

from qubit import qubit
from gates import XGate

def update(frame, fig, ax, q:qubit):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    q.phi = frame * 2*np.pi

    q.set_state(q.theta, q.phi)
    q.draw_bloch_sphere()
    q.draw_state()
    return

if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('equal')
    ax.axis('off')
    ax.title.set_text('Qubit State Animation')

    q = qubit(fig, ax)
    q.set_state(np.pi/4, 0)

    q.draw_bloch_sphere()

    ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), fargs=(fig, ax, q), interval=1, blit=False)
    ani.save('qubit_animation.gif', writer='imagemagick', fps=30)
    # plt.show()