import numpy as np
from qubit import qubit


def XGate(q:qubit):
    # Apply X gate to qubit

    X = np.array([[0, 1], 
                  [1, 0]])
                  
    phi_ = X @ q.get_psi()

    theta = 2*np.arccos(phi_[0])
    phi = np.angle(phi_[1])

    q.set_state(theta=theta, phi=phi)

def YGate(q:qubit):
    # Apply Y gate to qubit

    Y = np.array([[0, -1j], 
                  [1j, 0]])

    phi_ = Y @ q.get_psi()
    q.set_state(2*np.arccos(np.abs(phi_[0])), np.angle(phi_[1]))

def ZGate(q:qubit):
    # Apply Z gate to qubit

    Z = np.array([[1, 0], [0, -1]])
    phi_ = Z @ q.get_psi()
    q.set_state(2*np.arccos(np.abs(phi_[0])), np.angle(phi_[1]))


if __name__ == '__main__':

    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_aspect('equal')
    ax.axis('off')

    theta = np.pi/4
    phi = 0
    q = qubit(fig, ax, theta=theta, phi=phi, color='blue')
    q2 = qubit(fig, ax, theta=theta, phi=phi, color='k')

    q.draw_bloch_sphere()

    # XGate(q)
    YGate(q)
    # ZGate(q)

    q.draw_state()
    q2.draw_state()

    plt.show()