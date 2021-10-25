cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 12
===================================================================={cores['semestilo']}""")

print(f'{cores["vermelho"]}                        SISTEMA DE DESCONTO{cores["semestilo"]}')
preço = float(input(f'Qual o preço do produto? {cores["verde"]}R${cores["semestilo"]}'))
print(f'O valor do produto com {cores["vermelho"]}desconto{cores["semestilo"]} é de: {cores["verde"]}R$'
      f'{cores["semestilo"]}{preço*0.95:.2f}!')
print(f'{cores["azul"]}-'*67)
