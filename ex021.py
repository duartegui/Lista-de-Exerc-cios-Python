# Faça um programa em Python que abra e reroduza o áudio de um arquivo MP3.

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
resposta = 'outra' 
while resposta  != 'parar':
    resposta = input('Caso deseje parar a música digita parar: ')
mixer.music.stop 

