# Desenvolva um programa que leia o primeiro termo e a razão da uma PA. No final, mostre os 10 primeiros dessa
# progressão.

ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
contagemtermos = 0
print(f'Os 10 primeiros termos dessa Progressão Aritmética são:')
for c in range(ptermo, 100, razao):
    contagemtermos += 1
    if contagemtermos <= 10:
        print(c)



