from numpy import array, mat, sin, cos, exp
import numpy as np
from scipy.optimize import root
from sympy import solve, symbols, nsolve, Eq
import matplotlib.pyplot as plt
import xlwt,xlrd
def current0(eltaOER,eltaORR,E,j0):
    if E>=1.23:
        j=j0*exp(-alpha*F*(1.23-E)/(R*T)+(1.23-eltaOER)/(kb*T))
    else:
        j=-1*j0*exp(-alpha*F*(E-1.23)/(R*T)+(1.23-eltaORR)/(kb*T))
    return j
def current_standard(Gmax):
    j0=n*F*C_O*kb*T/h*exp(-Gmax/(kb*T))
    return j0
n=4 #transferred number
kb = 1.38e-23 * 6.24e18  # Boltzmann constant (eV)
T = 298.15 #Temperature
h = 4.136e-15  # Planck constant
F=9.649e4 #Faraday constant
R=8.314 #Gas molecular constant (J)
Gmax=0.21 #benchmark by Pt
C_O=1.488e-32 #benchmark by Pt
alpha=0.5
elta=np.arange(0.3,1.0,0.1)
E=np.arange(0,3,0.01)
matrix=[]
name=['1','2','3','4','5','6','7','8','9','BiN3O1','InO4']
OERelta=[0.38,0.39,0.38,0.30,0.64,0.81,0.45,0.49,0.78,1.07,1.42]
ORRelta=[0.39,0.51,0.70,0.35,0.25,0.33,0.53,0.45,0.48,0.48,0.52]
j0=current_standard(Gmax)
for i in range(len(name)):
    row=[]
    for j in range(len(E)):
        row.append(current0(OERelta[i],ORRelta[i],E[j],j0))
    matrix.append(row)
for i in range(len(matrix)):
    plt.plot(E, matrix[i], label="%s" % name[i])
plt.legend(prop={'size':9})
plt.ylim(-30,30)
plt.xlim(0,2.5)
x = [0, 2.5]
y = [10, 10]
plt.plot(x, y, linestyle='--', linewidth=2, color='black')
X = [0, 2.5]
Y = [-1, -1]
plt.plot(X, Y, linestyle='--', linewidth=2, color='black')
x1 = [1.23, 1.23]
y1 = [-30, 30]
plt.plot(x1, y1, linestyle='--', linewidth=1, color='red')
plt.xlabel("Potential (V vs RHE)",fontsize=14,fontweight='bold')
plt.ylabel("j (mA/cm2)",fontsize=14,fontweight='bold')
plt.savefig(r"./OER-ORR-factj.png")
plt.show()


