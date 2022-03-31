from oilprop.volumetric_thermal_expansion_coefficient import volumetric_thermal_expansion_coefficient as av
rho20 = 850  # kg/m3
t = 5  # Celsius degree
zeta = av(rho=rho20)  #  1/Celsius degree
rho5 = rho20 * (1 + zeta * (20 - t))
print(rho5)
