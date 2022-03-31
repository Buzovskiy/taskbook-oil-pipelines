from oilprop.volumetric_thermal_expansion_coefficient import volumetric_thermal_expansion_coefficient as av
from math import pi
from scipy.optimize import fsolve


rho20 = 730
t0 = 15
D = 5
L = 50
d = 2
H = 3
x0 = 1
t1 = 10


def rho(t):
    return rho20*(1 + av(rho20)*(20-t))


Vts = pi*(D ** 2)*L/4
Vg0 = (pi * d ** 2) * (H-x0)/4
# 5592
G0 = (Vts + Vg0) * rho(t0)

def G1(x1):
    return (Vts + (pi * d ** 2 / 4) * (H - x1)) * rho(t1)


def g0g1(x1):
    return G0 - G1(x1)

z = fsolve(g0g1, 10)
print(z)
