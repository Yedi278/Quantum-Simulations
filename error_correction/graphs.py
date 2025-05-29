import numpy as np
import matplotlib.pyplot as plt

# create a mash grid sphere

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

theta, phi = np.meshgrid(theta, phi)

x = np.cos(phi) * np.sin(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(theta)

r_1 = [
    np.cos(phi) * np.sin(theta),
    np.sin(phi) * np.sin(theta),
    np.cos(theta)
    ]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(*r_1 , color='b', alpha=0.1)

y = 0.9

r_2 = [
    (1 -y) * np.cos(phi) * np.sin(theta),
    (1 -y) * np.sin(phi) * np.sin(theta),
    (1 -y) * np.cos(theta) + y
    ]

ax.plot_wireframe(*r_2, color='r', alpha=0.1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()