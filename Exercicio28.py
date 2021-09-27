import random
#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5. Peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
print("""===========================================================================================================
                                          JOGO DA ADVINHAÇÃO
===========================================================================================================""")
numero = int(input('Escolha um número entre 0 e 5: '))
pensado = random.randint(0, 5)

if numero == pensado:
    print(f'Você me pegou! O número que eu estava pensando é {pensado}!')
else:
    print(f'Sinto muito, o número que eu estava pensando é {pensado}!'
          f'\nVocê não advinhou o número em que eu estava pensando!')

print('Tente mais uma vez! E tente ler a minha mente!')
