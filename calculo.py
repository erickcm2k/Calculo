import numpy as np
import matplotlib.pyplot as plt

datos = np.arange(0, 360)
datos = np.radians(datos)
datos = 3*np.sin(datos)

plt.plot(datos,"b") #usando b-- se imprime seccionada la gráfica
plt.show() #función que imprime la gráfica
#plt.savefig("Gráfica1.png") #función que guarda la gráfica
