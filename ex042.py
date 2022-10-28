# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

l1 = float(input('Digite o tamanho de um dos lados: '))
l2 = float(input('Digite o tamanho de outro lado: '))
l3 = float(input('Digite o tamanho do último lado: '))
n = ''


if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Os segmentos podem formar um triângulo.', end='')
    if l1 == l2 or l1 == l3 or l3 == l2:
   # if l1 == l2 == l3:
        print('O triângulo é equilátero')
    elif l1 != l2 != l3 != l1:
        print('O triângulo escaleno.')
    else:
        print('O triângulo é isóceles')
else:
    print('Os segmentos acima não podem formar um triângulo')
