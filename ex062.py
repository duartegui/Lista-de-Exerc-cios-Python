'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos'''

print('Gerador de PA')
print('=-=' * 15)
termoPA = int(input('Digite o valor do primeiro termo: '))
razaoPA = int(input('Digite o valor da razão da PA: '))
contador = 1
total = 0
termo = termoPA
mais = 10
while mais != 0:
    total = total + mais
    while  contador <= total:
        print(f'{termo} => ', end='')
        termo += razaoPA
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer colocar a mais?'))
print(f'FIM. Progressão finalizada com um total de {total} termos.')