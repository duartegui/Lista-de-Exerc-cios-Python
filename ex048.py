# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontrem
# no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
        cont += 1
        print(f'{c}')
print(f'O valor da soma de todos os {cont} números é: {soma}')
'''opção para dimiuir processamento.
    for c in range(1, 501, 2)
        soma = soma + c
        print(cont)'''
