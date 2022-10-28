 #Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

from random import randint
aposta = int(input('Tente advinhar o número de 0 a 5 que o computador escolheu:'))
numero = randint(0, 5) #sorteio de número inteiro
print('O número que eu escolhi foi {}'.format(numero))
if aposta == numero:
    print('Parabéns, você ganhou!')
else:
    print('Que pena, você perdeu!')
if aposta >= 6:
    print('O número que você digitou não existe entre 0 e 5!')
