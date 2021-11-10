from random import randint
import emoji
from time import sleep

cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'branco':'\033[1;97m', 'ciano':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 45
===================================================================={cores['semestilo']}""")

print(' '*25, emoji.emojize( f'{cores["branco"]}JO KEN PÔ:fist::hand::v:{cores["semestilo"]}', use_aliases=True))

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computer = randint(0, 2)

escolha = int(input(f"""Escolha:
{cores["vermelho"]}[ 0 ] Pedra{cores["semestilo"]}
{cores["verde"]}[ 1 ] Papel{cores["semestilo"]}
{cores["ciano"]}[ 2 ] Tesoura{cores["semestilo"]}
Digite sua opção: """))

print(f'{cores["branco"]}JO ', end='')
sleep(0.75)
print('KEN ', end='')
sleep(0.75)
print(f'PÔ!{cores["semestilo"]}')
sleep(0.75)

if escolha == 0 and computer == 0:
    print(f'EMPATE, o computador também escolheu {itens[computer]}.')
elif escolha == 0 and computer == 1:
    print(f'O computador venceu! Ele escolheu {itens[computer]}.')
elif escolha == 0 and computer == 2:
    print(f'Parabéns, você venceu! O computador escolheu {itens[computer]}.')
elif escolha == 1 and computer == 0:
    print(f'Parabéns, você venceu! O computador escolheu {itens[computer]}.')
elif escolha == 1 and computer == 1:
    print(f'EMPATE, o computador também escolheu {itens[computer]}')
elif escolha == 1 and computer == 2:
    print(f'O computador venceu! Ele escolheu {itens[computer]}.')
elif escolha == 2 and computer == 0:
    print(f'O computador venceu! Ele escolheu {itens[computer]}.')
elif escolha == 2 and computer == 1:
    print(f'Parabéns, você venceu! O computador escolheu {itens[computer]}.')
elif escolha == 2 and computer == 1:
    print(f'EMPATE, o computador também escolheu {itens[computer]}.')
else:
    print(f'Você digitou {escolha}, essa opção não faz parte da brincadeira! Tente novamente!')
