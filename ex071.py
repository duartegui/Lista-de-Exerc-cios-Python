'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=-='*10)
print('{:^30}'.format('BANCO DO HAJ'))
print('=-='*10)

saque = int(input('Qual o valor você quer sacar? R$'))
total = saque
cedula = 50
contagem_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        contagem_cedulas += 1
        
    else:
        if contagem_cedulas != 0:
            print(f'Você recebeu {contagem_cedulas} notas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contagem_cedulas = 0
        if total == 0:
            break
print('=-='*15)
print('{:^42}'.format('SAQUE FINALIZADO'))
print('=-='*15)

