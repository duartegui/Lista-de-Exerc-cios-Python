# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número pra saber se ele é um número primo: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes')
if total == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo')

