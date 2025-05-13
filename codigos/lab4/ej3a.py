import numpy as np
import os
import matplotlib.pyplot as plt

data_path = "../../datos/"

filename = "datos3a.dat"

file_path = os.path.join(data_path, filename)

#path = "../../datos/datos3a.dat"

datos = np.loadtxt(file_path)

x_fit = np.log(datos[0,:])
y_fit = np.log(datos[1,:])

p = np.polyfit(x_fit, y_fit, deg=1)

# p2 = np.polyfit(x_fit, y_fit, deg=3)

A = p[0]
C = np.exp(p[1]) # p[1] = ln(C)

x_plot = np.linspace(1,5,100)
y_plot = C*x_plot**A
#y_plot_2 = p2[0]* x_plot**3 + p2[1] * x_plot**2 + p2[2] * x_plot + p2[3]

plt.plot(datos[0,:], datos[1,:], ".r")
plt.plot(x_plot, y_plot)
#plt.plot(x_plot, y_plot_2)

plt.show()

print(f"{C = }, {A = }")

#print(p2)
