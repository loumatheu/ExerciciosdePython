cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 13
===================================================================={cores['semestilo']}""")

print(f'{cores["verde"]}                         REAJUSTE DE SALÁRIO{cores["semestilo"]}')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
nome = input('Digite o nome do funcionário: ').strip()
sa = float(input(f'Digite o salário atual do funcionário: {cores["verde"]}R${cores["semestilo"]}'))
print(f'O Sr(a). {cores["azul"]}{nome}{cores["semestilo"]} deixará de receber o valor de {cores["verde"]}R${sa:.2f}'
      f'{cores["semestilo"]} e passará a receber {cores["verde"]}R${sa*1.15:.2f}{cores["semestilo"]}!')
print(f'{cores["amarelo"]}Parabéns pelo aumento de 15%!{cores["semestilo"]}')
print(f'{cores["azul"]}-'*67)
