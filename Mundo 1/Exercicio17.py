import math
import emoji

print('=====================================')
print('           CHALLENGE 17')
print('=====================================')
print(emoji.emojize(':star: CALCULANDO A HIPOTENUSA DE UM TRIÂNGULO RETANGULO :star:', use_aliases=True))
catop = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.pow(catop, 2) + math.pow(catadj, 2)
print(f'A hipotenusa do triângulo em questão é: {math.sqrt(hip):.2f}')

#Metódo mostrado na aula:
#catetoop = float(input('Digite o comprimento do cateto oposto: '))
#catetoad = float(input('Digite o comprimento do cateto adjacente: '))
#hipotenusa = math.hypot(catetoop, catetoad)
#print(f'A hipotenusa do triângulo em questão é: {hipotenusa:.2f}')
