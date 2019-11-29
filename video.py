import sympy as sp
import numpy as np
#import matplotlib.pyplot as plt
#from scipy.misc import derivative


print("\nIngrese la funcion a derivar\n")
cadena = input()
x = sp.Symbol('x')


print("\nLa funcion ingresada es: ", cadena)
print("\nSu derivada es: ", sp.diff(cadena, x))
print("\nSu integral es: ", sp.integrate(cadena, x), "+ C\n")


"""
sudo apt install python3-pip
pip3 --version
sudo pip install numpy
sudo pip install sympy
sudo pip install matplotlib
sudo pip install scipy
"""
