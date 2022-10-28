'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = 'S'
maior = menor = contador = total = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    contador += 1
    total += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    resposta = input('Deseja digitar mais números?[S/N] ')
média = total / contador
print(f'A média dos {contador} números digitados é de {média}. O maior número digitado foi {maior} e o menor número digitado foi {menor}')

    

