# Faça um programa que leia o salário de funcionário e mostre o novo salário com 15% de aumento.
# Aprimorei o desafio colocando um input para que o usuário possa escolher a porcentagem a ser aplicada

s = float(input('Digite o salário do funcionário:'))
a = float(input('Digite a porcentagem do reajuste:'))
c1 = 100+a
c2 = s/100*c1
print('O valor do salário reajustado é de: {:.2f}'.format(c2))
