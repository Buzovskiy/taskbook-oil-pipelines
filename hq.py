import matplotlib.pyplot as plt
from pumps2 import Pumps

pump_w = Pumps('water')
pump_o = Pumps('oil')

Q = [_ * 100 for _ in range(0, 11, 1)]
Hw = [round(pump_w.head(Qw), 1) for Qw in Q]
Ho = [round(pump_o.head(Qo), 1) for Qo in Q]

fig, ax = plt.subplots()
ax.plot(Q, Hw, label='Напор по воде')
ax.plot(Q, Ho, label='Напор по нефти')
plt.xlabel('Q')
plt.ylabel('H')

ax.legend()

plt.show()
# print(1)