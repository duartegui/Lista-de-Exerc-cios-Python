# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostra:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
totmulher20 = 0
nomemaisvelho = ''

for c in range(1, 5):
    print(f'-----{c}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade/c
print(f'A média de idade do grupo é de {médiaidade} anos.')
print(f'O homem mais velho se chama {nomemaisvelho} e ele tem {maioridadehomem} anos.')
print(f'Ao todo são {totmulher20} mulheres com menosde 20 anos')

