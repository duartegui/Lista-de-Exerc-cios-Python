'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

catalogo = ('Lapis', 1.75, 
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 12,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)
for posicao in range(0, len(catalogo)):
    if posicao % 2 ==0:
        print(f'{catalogo[posicao]:.<30}', end='')
    else:
       print(f'R$ {catalogo[posicao]:>7.2f}')
print('-' * 40)