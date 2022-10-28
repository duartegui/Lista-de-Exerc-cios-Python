#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distância do destino em KM:'))
longa = distancia * 0.45
curta = distancia * 0.5
if distancia <= 200:
    print('O valor da viagem será: R${}'.format(curta))
else:
    print('O valor da viagem será: R${}'.format(longa))


