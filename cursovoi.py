import math
from pumps import Pumps
import matplotlib.pyplot as plt

L1 = 75  # km
L2 = 30
L3 = 25
Gnppab = 3031000
Gnppdt = 4791000
Gnb = 50000
rho_ab = 730
rho_dt = 820
nu_ab = 1 * 10 ** -6
nu_dt = 6 * 10 ** -6
D = 530e-3  # m
delta = 10e-3  # m
d = D - 2 * delta  # m
Kp = 1.5

S = math.pi * d ** 2 / 4  # m2

Qnppab = Gnppab * 1000 / (rho_ab * 365 * 24 * 60 * 60)  # m3/s
Qnppdt = Gnppdt * 1000 / (rho_dt * 365 * 24 * 60 * 60)  # m3/s

w_ab = Qnppab / S  # m/s
w_dt = Qnppdt / S  # m/s

Gnb_dt = round(Gnb / Kp, -3)
Gnb_ab = Gnb - Gnb_dt

print(Qnppdt * 3600)

ND10 = Pumps('ND10')
print(f'H0 = {ND10.H0}\n a = {ND10.a}\n b = {ND10.b}')
MN1250 = Pumps('NM1250-260')
print(f'H0 = {MN1250.H0}\n a = {MN1250.a}\n b = {MN1250.b}')


Q_ND10 = [_ * 100 for _ in range(0, 11, 1)]
H_ND10 = [round(ND10.head(Q), 1) for Q in Q_ND10]
print(H_ND10)

fig, ax = plt.subplots()
ax.plot(Q_ND10, H_ND10)
plt.show()
