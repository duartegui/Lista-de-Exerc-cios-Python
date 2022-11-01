'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre: A) Quantas pessoas tem mais de 18 anos.
                            B) Quantos homens foram cadastrados
                            C) Quantas mulheres tem menos de 20 anos'''
from tkinter import N


maior_idade = homens_cadastrados = idade_mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa[M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        idade_mulher += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Foram inclusas {maior_idade} pessoas com mais de 18 anos, {homens_cadastrados} homens e {idade_mulher} mulheres com menos de 20 anos')
print('Acabou')

