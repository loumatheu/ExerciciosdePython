from time import sleep
import emoji

cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'branco':'\033[1;97m', 'ciano':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 45
===================================================================={cores['semestilo']}""")

print(f'{cores["branco"]}CONTAGEM REGRESSIVA{cores["semestilo"]}')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(f':tada::fireworks:FELIZ ANO NOVOOOO!:fireworks::tada:', use_aliases=True))
