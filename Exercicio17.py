import math
import emoji

print('=====================================')
print('           CHALLENGE 17')
print('=====================================')
print(emoji.emojize(':star: CALCULANDO A HIPOTENUSA DE UM TRIÂNGULO RETANGULO :star:', use_aliases=True))
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hip = math.pow(catop, 2) + math.pow(catadj, 2)
print(f'A hipotenusa do triângulo em questão é: {math.sqrt(hip):.2f}')
