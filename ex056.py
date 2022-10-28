# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostra:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

maioridade = 0
nomemaisvelho = ''
sexomaisvelho = ''
contador = 0
contfeminino = 0
sexo = ''
idade = 0
for i in range(1, 5):
    contador += 1
    coletanome = input(f'Digite o nome da {contador}º pessoa: ')
    coletasexo = input(f'Digite o sexo da {contador}ª pessoa: ')
    coletaidade = input(f'Digite a idade da {contador}ª pessoa: ')

    if i == 1:
        maioridade = coletaidade
        nomemaisvelho = coletanome
        sexomaisvelho = coletasexo

    else:
        if coletaidade > maioridade and coletasexo in 'masculino':
            maioridade = coletaidade
            nomemaisvelho = coletanome
        elif coletaidade < 20 and coletasexo in 'feminino':
            contfeminino += 1


idade += coletaidade
mediaidade = idade / contador
print(f'A média das idades é: {mediaidade}')
print(f'O homem mais velho se chama {nomemaisvelho} e tem {maioridade} anos.')
print(f'Existem {contfeminino} mulheres com menos de 20 anos.')
