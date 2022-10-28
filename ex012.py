# Faça um programa que leia o preço de um produto e exiba o novo preço com 5% de desconto
p = float(input('Digite o preço do produto: R$'))
print('O novo preço com 5% de desconto é de: R${:.2f}'.format(p/100*95))

