from math import radians, cos, sin, tan, trunc
import emoji

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 18
===================================================================={cores['semestilo']}""")

print(emoji.emojize(':star: CALCULANDO SEN, COS E TAN DE UM ÂNGULO QUALQUER :star:', use_aliases=True))

ang = float(input('\nDigite o valor do ângulo: '))
print(f'O seno do ângulo {trunc(ang)}º é igual a: {sin(radians(ang)):.2f}')
print(f'O cosseno do ângulo {trunc(ang)}º é igual a: {cos(radians(ang)):.2f}')
print(f'A tangente do ângulo {trunc(ang)}º é igual a: {tan(radians(ang)):.2f}')
