#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
cid = str(input('Em qual cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')

