'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Fortaleza.
'''
times = ('Palmeiras','Internacional','Fluminense','Corinthians',
        'Flamengo','Athletico-PR','Atlético-MG','Fortaleza',
        'São Paulo','América-MG','Botafogo','Santos','Goiás',
        'Bragantino','Cortiba','Cuiabá','Ceará SC','Atlético-GO',
        'Avaí','Juventude',)

print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' * 15)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Times organizados em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O time Fortaleza está na posição {times.index("Fortaleza")+1}')
