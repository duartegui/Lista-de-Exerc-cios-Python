# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite o número que você quer que seja convertido:'))
print('''Escolha uma das bases para conversão:
[1] Converter para binário.
[2] Converter para octal.
[3] Converter para hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a:{}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')

