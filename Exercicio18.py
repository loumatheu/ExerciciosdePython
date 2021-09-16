from math import radians, cos, sin, tan, trunc
import emoji

print('=====================================')
print('           CHALLENGE 18')
print('=====================================')
print(emoji.emojize(':star: CALCULANDO SEN, COS E TAN DE UM ÂNGULO QUALQUER :star:', use_aliases=True))

ang = float(input('\nDigite o valor do ângulo: '))
print(f'O seno do ângulo {trunc(ang)}º é igual a: {sin(radians(ang)):.2f}')
print(f'O cosseno do ângulo {trunc(ang)}º é igual a: {cos(radians(ang)):.2f}')
print(f'A tangente do ângulo {trunc(ang)}º é igual a: {tan(radians(ang)):.2f}')
