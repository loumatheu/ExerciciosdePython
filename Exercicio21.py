from pydub import AudioSegment
from pydub.playback import play
from emoji import emojize

print('=====================================')
print('           CHALLENGE 20')
print('=====================================')
print(emojize(':musical_note: MP3 Player :notes:', use_aliases=True))

print('Reproduzindo a melhor música do dia:')
music = AudioSegment.from_mp3('musica.mp3')
play(music)

NÃO RESOLVIDO