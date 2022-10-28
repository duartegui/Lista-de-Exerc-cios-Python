# Escreva um programa que pergunte a quantidade de km percorridas por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
d = int(input('Digita a quantidade de dias que o carro foi alugado:'))
km = float(input('Digite a quantidade de km percorrida pelo carro:'))

t = (d*60) + (km*0.15)

print('O custo do aluguel dessas cndições é de: R${:.2f}'.format(t))
