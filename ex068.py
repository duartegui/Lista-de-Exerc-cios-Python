'''Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mistrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
contador = 0
while True:
    numero_computador = randint(0,10)
    numero_humano = int(input('Digite um número: '))
    opcao_humano = str(input('Digite se quer Par ou Ímpar [P/I]:')).strip().upper()[0]

    
    if opcao_humano in ('P'):
        if (numero_humano + numero_computador) % 2 != 0:
            print(f'O computador digitou {numero_computador} e você digitou {numero_humano}. Você perdeu!')
            print(f'Você teve uma sequência de {contador} acertos')
            break
        else:
            print(f'O computador digitou {numero_computador} e você digitou {numero_humano}.Você ganhou!')
            contador += 1
            print('-' * 10)
    if opcao_humano in ('I'):
        if (numero_humano + numero_computador) % 2 != 0:
            print(f'O computador digitou {numero_computador} e você digitou {numero_humano}.Você ganhou!')
            contador += 1
        else:
            print(f'O computador digitou {numero_computador} e você digitou {numero_humano}. Você perdeu!')
            print(f'Você teve uma sequência de {contador} acertos')
            break

