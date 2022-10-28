# Converta a temperatura de celsius para fahreinheit e kelvin
tc = float(input('Digite a temperatura e °C:'))
F = tc/5 * 9 + 32
K = tc/5 * 5 + 273
print('A temperatura em graus fahreinheit é de:{:.2f}°F\nE a teperatura em Kelvin é de:{:.2f}K'.format(F, K))
