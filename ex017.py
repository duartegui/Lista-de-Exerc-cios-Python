# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = (float(input('Digite o valor do cateto adjacente: ')))
'''hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) #elevar a meio é uma forma de calcular a raiz quadrada de um número

print(f'O valor da hipotenusa é: {hipotenusa:.2f}')''' #essa é a forma de resolver realizando os cálculos matemáticos

hipotenusa = math.hypot (cateto_oposto, cateto_adjacente)
print(f'O valor da hipotenusa é de: {hipotenusa:.2f}') #essa foi a forma de resolver usando a biblioteca math
