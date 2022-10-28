# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Digite sua data de nascimento:'))
atual = date.today().year # data atual
diferenca = (atual - ano) - 18
if diferenca < 0:
    print('Você ainda não pode se alistar. Faltam {} ano(s).'.format(diferenca * -1))
    print('Seu alistamento vai ser em {}'.format(atual + (diferenca * -1)))
elif diferenca > 0:
    print('Você já passou {} ano(s) do ano de alistamento. Favor se apresentar urgentemente.'.format(diferenca))
    print('Seu alistamento foi em {}.'.format(atual - diferenca))
else:
    print('Você precisa se alistar esse ano.')
