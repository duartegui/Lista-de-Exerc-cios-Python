# Crie um programa que leia seu dobro, seu triplo e raiz quadrada.
v = int(input('Digite o valor a ser cálculado:'))
#d = v * 2
#t = v * 3
#r = v ** (0.5)
#print('O dobro de {0} é {1} e o triplo de {0} é {2}! \nE a raiz quadrada de {0} é {3:.2f}.'.format(v, d, t, r))
#print('O dobro de {0} é {1}, o triplo de {0} é {2} e
# a raiz quadrada de {0} é {3:.2f}.'.format(v, (v*2), (v*3),(v**(1/5))))

print('O dobro de {} vale {}'.format(v, (v*2)))
print('O triplo de {} vale {}\nE a raiz quadrada de {} é igual a {:.2f}.'.format(v, (v*3), v, (pow(v, (1/2)))))
