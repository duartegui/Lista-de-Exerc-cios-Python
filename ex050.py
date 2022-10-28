# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, se o valor
# digitado for ímpar, desconsidere-o
cont = 0
soma = 0
print('Digite 6 números.')
for c in range(1, 7):
    n = int(input(f'Digite o número {c}: '))
    if n % 2 == 0:
        cont = cont + 1
        soma += n
print(f'Você digitou {cont} números pares e a soma é: {soma}')
