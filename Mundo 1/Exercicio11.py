cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 11
===================================================================={cores['semestilo']}""")

print(f'{cores["verde"]}                         PAINT MESUAREMENT{cores["semestilo"]}')
print('Quantos litros de tinta eu preciso para pintar uma parede?')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
b = float(input(f'Digite a {cores["verdepiscina"]}largura{cores["semestilo"]} da sua parede em metros: '))
h = float(input(f'Digite a {cores["verdepiscina"]}altura{cores["semestilo"]} da sua parede em metros: '))
tinta = (b*h)/2
a = (b*h)
print(f'A área da parede é de {cores["amarelo"]}{a:.2f}m²{cores["semestilo"]} e serão necessários aproximadamente '
      f'{cores["vermelho"]}{tinta:.1f}L'
      f'{cores["semestilo"]}  de tinta para pintá-la completamente!')
print(f'{cores["azul"]}-'*67)
