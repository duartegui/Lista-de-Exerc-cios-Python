'''Crie um programa que leia dois valores e mostre um menu como abaixo:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''

from time import sleep
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
opcao = 0

while  opcao != 5:
    opcao = int(input('''\nEscolha uma das opções abaixo:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa: \n'''))
    sleep(1)
    print('=-=' * 15)
    if opcao == 1:
        print(f'O resultado da soma de {valor1} com {valor2} é: {valor1 + valor2}')
    elif opcao == 2:
        print(f'O resultado da multiplicação de {valor1} com {valor2} é: {valor1 * valor2}')
    elif opcao == 3:
        if valor1 < valor2:
            print(f'O número {valor2} é maior que o número {valor1}')
        elif valor2 < valor1:
            print(f'O número {valor2} é menor que o número {valor1}')
        else:
            print('Os valores são iguais.')
    elif opcao == 4:
        valor1 = int(input('Digite um novo primeiro valor:'))
        valor2 = int(input('Digite um novo segundo valor:'))
    elif opcao == 5:
        print('A aplicação foi encerrada.')
    else:
        print('Opção inválida, digite novamente.')