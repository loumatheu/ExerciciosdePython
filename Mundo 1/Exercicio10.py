cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 10
===================================================================={cores['semestilo']}""")

print(f'{cores["verde"]}                      Conversor de moedas ${cores["semestilo"]}')
carteira = float(input(f'Quantos reais você tem? {cores["verde"]}R${cores["semestilo"]}'))
print(f'{cores["azul"]}-{cores["semestilo"]}'*60)
dollar = (carteira / 4.94)
euro = (carteira / 5.88)
canadiandollar = (carteira / 3.98)
libraesterlina = (carteira / 6.84)
print(f'Você pode obter as seguintes moedas com o seu dinheiro atual: {cores["verde"]}R${carteira:.2f}{cores["semestilo"]}!')
print(f'Dólar Estadunidense: {cores["azul"]}US${dollar:.2f}{cores["semestilo"]}')
print(f'Euro: {cores["amarelo"]}€{euro:.2f}{cores["semestilo"]}')
print(f'Dólar Canadense: {cores["vermelho"]}CAD${canadiandollar:.2f}{cores["semestilo"]}')
print(f'Libra esterlina: {cores["lilas"]}£{libraesterlina:.2f}{cores["semestilo"]}')
print(f'{cores["azul"]}-{cores["semestilo"]}'*60)
print(f'{cores["azul"]}-'*67)
