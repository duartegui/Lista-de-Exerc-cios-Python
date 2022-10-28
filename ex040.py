# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a seugunda nota:'))

m = (n1 + n2) / 2

if m < 5.0:
    print('Média abaixo de 5.0, você foi reprovado.')
elif 7 > m >= 5:
    print('Média entre 5.0 e 6.9, você está de recuperação.')
else:
    print('Média 7.0 ou superior, você foi aprovado.')

