# Escreve uma programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
v = int(input('Digite o valor em métros:'))
# print('O valor convertido em centímetros é:{}'.format(v*100))
# print('O valor convertido em milímetros é:{}'.format(v*1000))
print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(v, v/1000, v/100, v/10, v*10, v*100,
                                                                                   v*1000))
