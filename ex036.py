# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

vcasa = float(input('Olá, qual o valor da casa a ser comprada? R$:'))
salario = float(input('Agora digite o valor do seu salário:'))
anos = int(input('Por fim diga em quantos anos pretende quitar o imóvel:'))

psalario = salario / 100 * 30
prestação = vcasa / (anos*12)

if prestação <= psalario:
    print('Parabéns, seu parcelamento no valor de R${:.2f} mensais foi aprovado.'.format(prestação))
else:
    print('Para pagar esse imóvel em {} anos a parcela será de R${:.2f}, porém esse valor excede 30% do seu salário'
          ' atual. Empréstimo NEGADO!'.format(anos, prestação))



