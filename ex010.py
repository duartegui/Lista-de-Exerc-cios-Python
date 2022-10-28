#Escreve uma programa que leia o quanto a pessoa tem na carteira e diga a quantidade
# em dólares que você pode comprar com esse valor. Considere o dólar cotado em R$3,27
v = float(input('Digite o valor que possui na carteira: R$'))
print('O valor em dólares que você pode adquirir com R${} é de:${:.2f}'.format(v, v/5.18))

