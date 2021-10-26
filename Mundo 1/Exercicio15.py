cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 15
===================================================================={cores['semestilo']}""")

print(f'{cores["verde"]}                         ALUGUEL DE CARROS{cores["semestilo"]}')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
km = float(input('Digite a distância percorrida em Km: '))
dias = int(input('Por quantos dias o veículo foi alugado? '))
total = (60*dias) + (0.15*km)
print(f'O total a pagar é de {cores["verde"]}R${total:.2f}{cores["semestilo"]}!')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
