'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
total_compra = produtos_alto_preco = produto_menor_preco = 0
nome_menor_preco = ''
cont = 0
while True:
    produto = str(input('Digine o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))
    cont += 1
    total_compra += preco
    if preco > 1000:
        produtos_alto_preco += 1
    if cont == 1 or preco < produto_menor_preco:
        produto_menor_preco = preco
        nome_menor_preco = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {total_compra:.2f}.')
print(f'Você adicionou {produtos_alto_preco} produto(s) que custam mais de 1000 reais.')
print(f'O produto de menor preço foi {nome_menor_preco} e custou R${produto_menor_preco}')
