'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input('Digite o primeiro valor:')),
            int(input('Digite o segundo valor:')),
            int(input('Digite o terceiro valor:')),
            int(input('Digite o último valor:')))
print(f'Você digitou os números {numeros}.')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram: ', end=' ')
for c in numeros:
    if c % 2 ==0:
        print(c, end=' ')
