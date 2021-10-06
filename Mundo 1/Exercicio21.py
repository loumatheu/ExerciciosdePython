from pygame import mixer
from emoji import emojize

print('=====================================')
print('           CHALLENGE 20')
print('=====================================')
print(emojize(':musical_note: MP3 Player :notes:', use_aliases=True))

print('Reproduzindo a melhor música do dia:')
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()

input('Pressione enter para encerrar: ')
