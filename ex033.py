#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número entre os digitados foi: {}'.format(menor))
if b > a and b > c:
    maior = b
if c > a and C > b:
    maior = c
print('O maior número entre os digitados foi: {}'.format(maior))


