import math
import emoji

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 17
===================================================================={cores['semestilo']}""")

print(emoji.emojize(f'{cores["amarelo"]}:star:{cores["semestilo"]} CALCULANDO A HIPOTENUSA DE UM TRIÂNGULO RETANGULO '
                    f'{cores["amarelo"]}:star:{cores["semestilo"]}', use_aliases=True))
catop = float(input(f'Digite o comprimento do {cores["vermelho"]}cateto oposto{cores["semestilo"]}: '))
catadj = float(input(f'Digite o comprimento do {cores["verdepiscina"]}cateto adjacente{cores["semestilo"]}: '))
hip = math.pow(catop, 2) + math.pow(catadj, 2)
print(f'A hipotenusa do triângulo em questão é: {cores["verde"]}{math.sqrt(hip):.2f}')

#Metódo mostrado na aula:
#catetoop = float(input('Digite o comprimento do cateto oposto: '))
#catetoad = float(input('Digite o comprimento do cateto adjacente: '))
#hipotenusa = math.hypot(catetoop, catetoad)
#print(f'A hipotenusa do triângulo em questão é: {hipotenusa:.2f}')
