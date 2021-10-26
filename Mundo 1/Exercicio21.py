from pygame import mixer
from emoji import emojize

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 21
===================================================================={cores['semestilo']}""")

print(emojize(':musical_note: MP3 Player :notes:', use_aliases=True))

print('Reproduzindo a melhor música do dia:')
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()

input('Pressione enter para encerrar: ')
