# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome dela

nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
