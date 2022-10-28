# Escreva um programa que leia a velocidade de um carro, sele eultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('PARE! Você excedeu o limite de velocidade que é de 80km/h e foi multado em R${}'.format(multa))
    print('Dirija com segurança!')
print('Tenha um bom dia, continue dirigindo em segurança!') #Não foi colocado else, por essa foi uma condição simples.
