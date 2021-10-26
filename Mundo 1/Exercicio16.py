from math import floor
cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 16
===================================================================={cores['semestilo']}""")

print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
num = float(input('Digite um número real e veja sua parte inteira: '))
print(f'A parte inteira de {num} é {floor(num)}.')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
