# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.

maior = 90.2
menor = 48.9
contador = 0
for coleta in range(1, 5):
    contador += 1
    peso = float(input(f'peso da {contador}ª pessoa:'))
    if coleta == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é:{maior}Kg \nO menor peso é:{menor}Kg')
