cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 06
===================================================================={cores['semestilo']}""")

print('Descrubra qual o dobro, triplo e raiz quadrada do número desejado!')
num = int(input('Digite um valor numérico: '))
print(f'O dobro de {cores["verde"]}{num}{cores["semestilo"]} é {cores["lilas"]}{num*2}{cores["semestilo"]}, o seu '
      f'triplo é {cores["amarelo"]}{num*3}{cores["semestilo"]} e sua raiz quadrada é {cores["vermelho"]}{num**(1/2)}'
      f'{cores["semestilo"]}!')
print(f'{cores["azul"]}-'*67)
