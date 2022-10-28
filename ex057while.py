sexo = str(input('Digite se sexo[M/F]:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Valor inválido, digite seu sexo novamente:')).strip().upper()[0]
if sexo == 'M':
    print('O sexo masculino foi registrado com sucesso!')
else:
    print('O sexo feminino foi registrado com sucesso!')

