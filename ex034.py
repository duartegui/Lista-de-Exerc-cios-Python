#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário do funcionário: R$"))

if salario <= 1250.00:
    novo = salario + (salario / 100 * 15)
else:
    novo = salario + (salario / 100 * 10)
print('Quem ganhava R${:.2f} após o aumento passou a ganhar: R${:.2f}'.format(salario, novo))

