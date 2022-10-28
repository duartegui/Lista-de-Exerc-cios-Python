# Digite algo e mostre o tipo primitivo e todas as informações disponíveis sobre o que foi digitado

algo = input('Digite algo:')
###print('O tipo primitivo desse valor é', type(algo))
###print('Só tem espaços?', algo.isspace())
###print('É alfabético?', algo.isalpha())
###print('É numérico?', algo.isnumeric())
###print('É alfanumérico?', algo.isalnum())
###print('Está em maiúsculas?', algo.isupper())
###print('Está em minúsculas?', algo.islower())
###print('Está captalizada?', algo.istitle())

print('O tipo primitivo desse valor é:', type(algo))
print('Só tem espaços? {}'.format(algo.isspace(),
      '\nÉ alfabético? {}'.format(algo.isalpha()),
      '\nÉ alfanumérico? {}'.format(algo.isalnum()),
      '\nÉ numérico? {}'.format(algo.isnumeric()),
      '\nEstá em maiúsculas? {}'.format(algo.isupper()),
      '\nEstá em minúsculas? {}'.format(algo.islower()),
      '\nEstá captalizado? {}'.format(algo.istitle())))
