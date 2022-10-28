# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maior idade e quantas já são maiores.

from datetime import datetime

maior = 0
menor = 0
hoje = datetime.today().year
contador = 0
for coleta in range(1, 8):
    contador += 1
    data = int(input(f'Digite o ano de nascimento da {contador}° pessoa aqui:'))
    calculo = hoje - data
    if calculo >= 18:
        maior += 1
    else:
        menor += 1
print(f' {maior} pessoas são maiores de idade, enquanto {menor} são menores de idade')
