'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo'''

contador = 0

while True:
    numero = int(input('Digite um número para ver a tabuada dele: '))
    if numero < 0:
        break
    print('-'*10)
    while True:
        if contador == 10:
            contador = 0
            break
            
        contador += 1
        resultado = numero * contador
        print(f'{numero} x {contador} = {resultado}')
    print('-'*10)
print('Fim do programa.')
