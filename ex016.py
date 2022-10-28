''' Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
 Ex: Digiteum número: 6.127
 O múmero 6.127 tem sua parte inteira 6.'''

import math
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, math.trunc(n)))
