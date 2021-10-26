from random import randint
from time import sleep
#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5. Peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 28
===================================================================={cores['semestilo']}""")

print(f"""{cores['amarelo']}====================================================================
                         JOGO DA ADVINHAÇÃO
===================================================================={cores['semestilo']}""")
print('Em qual número estou pensando?')
numero = int(input('Escolha um número entre 0 e 5: '))
pensado = randint(0, 5)
print('Processando...')

sleep(2)

if numero == pensado:
    print(f'Você me pegou! O número que eu estava pensando é {pensado}!')
else:
    print(f'Sinto muito, o número que eu estava pensando é {pensado}!'
          f'\nVocê não advinhou o número em que eu estava pensando!')

print('Tente mais uma vez! E tente ler a minha mente!')
