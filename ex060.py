from math import factorial
numero = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}')
print(f'O fatorial de {numero} é {fatorial}')

#Forma de fazer sem a biblioteca:
'''numero = int(input('Digite um número para calcular seu Fatorial: '))
contador = numero
fatorial = 1
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else' = ', end='' )
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')'''

