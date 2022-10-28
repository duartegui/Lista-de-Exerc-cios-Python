# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.
# Observação: cada comprimeoto precisa ser menor do que a soma do comprimento dos outros dois
print('-='*20)
print('Analisador de triângulos.')
print('-='*20)
l1 = float(input('Digite o comprimeto da primeira reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da terveira rea: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Essas 3 retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')

