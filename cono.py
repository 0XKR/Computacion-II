import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Configurar la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#generar el cono
theta = np.linspace(0, 2*np.pi, 100)
z = np.linspace(0, 2, 100)
theta, z = np.meshgrid(theta, z)
x = np.cos(theta) * (z/2)
y = np.sin(theta) * (z/2)

#Trazar el cono
ax.plot_surface(x, y, z, color='b', alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Tanque conico radio 1, altura 2')

#mostrar
plt.show()
