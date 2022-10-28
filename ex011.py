# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessário para pintá-la. Sabendo que cada litro de tinta pinta
# uma área de 2 metros quadrados
alt = float(input('Digite a altura da parede:'))
lar = float(input('Digite a largura daparede:'))
# Não nomear variáveis com l, O ou i. Por parecer um número a sintaxe reclama
a = alt*lar
print('Sua parede tem a dimensão de {} x {} e  sua área é de {}m²'.format(alt, lar, a))
print('A quantidade de tinta necessária pra printar essa parede é:{}L'.format(a/2))
