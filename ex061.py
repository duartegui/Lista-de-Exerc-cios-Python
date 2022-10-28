'''Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('Gerador de PA')
print('=-=' * 15)
termoPA = int(input('Digite o valor do primeiro termo: '))
razaoPA = int(input('Digite o valor da razão da PA'))
contador = 1
termo = termoPA
while  contador <= 10:
    print(f'{termo} => ', end='')
    termo += razaoPA
    contador += 1
print('FIM')