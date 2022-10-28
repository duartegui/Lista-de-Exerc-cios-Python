'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

contador = soma = 0 #forma de atribuir o mesmo valor à variáveis diferentes

print('=-='*20)
print('Tratando vários valores')
print('=-='*20)
valor = int(input('Digite uma valor para ser somado: ')) #Mesmo comando que está dentro do while pra evitar ter que subtrair o valor 999 da variável soma na hora de exibir. 


while valor != 999:
    soma += valor
    contador += 1
    valor = int(input('Digite uma valor para ser somado: '))
print(f'código de parada digitado. Você digitou {contador} números e a soma entre eles é {soma}')
