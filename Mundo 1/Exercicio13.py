cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 13
===================================================================={cores['semestilo']}""")

print(f'{cores["verde"]}                         REAJUSTE DE SALÁRIO{cores["semestilo"]}')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
nome = input('Digite o nome do funcionário: ')
sa = float(input('Digite o salário atual do funcionário: R$'))
print(f'O Sr(a). {nome} deixará de receber o valor de R${sa} e passará a receber R${sa*1.15:.2f}!')
print('Parabéns pelo aumento de 15%!')
print(f'{cores["azul"]}-'*67)