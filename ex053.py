# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase = str(input("Digite uma frase: ")).strip().upper()
invertidosemjuntar = (frase[::-1])
palavras = frase.split()
juntar = ''.join(palavras)
invertido = (juntar[::-1])
if invertido == juntar:
    print(f'A frase {frase} e a frase {invertidosemjuntar} são palíndromos.')
else:
    print(f'A frase {frase} e a frase {invertidosemjuntar} não são palíndromos.')

