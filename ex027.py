# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
# primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza,  primeiro = Ana e último = Souza
nome = str(input('Digite seu nome completo:')).strip()
nome2 = nome.split()
print('Seu primeiro nome é {}'.format(nome2[0]))
print('Seu último nome é {}'.format(nome2[len(nome2)-1]))

