import math
import emoji

print('=====================================')
print('           CHALLENGE 18')
print('=====================================')
print(emoji.emojize(':star: CALCULANDO SEN, COS E TAN DE UM ÂNGULO QUALQUER :star:', use_aliases=True))

ang = float(input('\nDigite o valor do ângulo: '))
print(f'O seno do ângulo {math.trunc(ang)}º é igual a: {math.sin(ang)}')
print(f'O cosseno do ângulo {math.trunc(ang)}º é igual a: {math.cos(ang)}')
print(f'A tangente do ângulo {math.trunc(ang)}º é igual a: {math.tan(ang)}')
