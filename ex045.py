# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma opção:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 15)
print('O Jogador escolheu: {}'.format(itens[jogador]))
print('O computador escolheu: {}'.format(itens[computador]))
print('-=' * 15)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence.')
    elif jogador == 2:
        print('Computador vence.')
    else:
        print('Opção inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence.')
    else:
        print('Opção inválida.')
if computador == 2:
    if jogador == 0:
        print('Jogador venceu.')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção inválida.')




