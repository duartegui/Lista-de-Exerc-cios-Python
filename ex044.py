# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juro

print('{:=^40}'.format('Lojas Duarte'))
preco = float(input('Digite o valor da compra: '))
opcao = int((input('Escolha a opção de forma de pagamento:\n'
                   '[1] à vista dinheiro/cheque\n'
                   '[2] à vista no cartão\n'
                   '[3] em até 2x no cartão\n'
                   '[4] 3x ou mais no cartão\n'
                   'Qual a opção? ')))

if opcao == 1:
    print('O valor com desconto vai ser de: {:.2f}'.format(preco - (preco * 10 / 100)))
elif opcao == 2:
    print('O valor com desconto vai ser de: {:.2f}'.format(preco - (preco * 5 / 100)))
elif opcao == 3:
    parcela = preco / 2
    print('Essa forma de pagamento não possui desconto, ficando assim no valor de R${} a parcela'.format(parcela))
elif opcao == 4:
    nparcelas = int(input('Quanatas parcelas? '))
    precototal = preco + (preco * 20 / 100)
    parcela = precototal / nparcelas
    print('Parcelando em {} vezes de {} e o valor total com juros vai ser de {}'.format(nparcelas, parcela, precototal))

else:
    print('Opção inválida')
