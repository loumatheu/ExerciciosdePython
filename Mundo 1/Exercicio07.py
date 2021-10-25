cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 07
===================================================================={cores['semestilo']}""")

print(f'                    {cores["azul"]}SISTEMA DE NOTAS ESTUDANTIS{cores["semestilo"]}')
n1 = float(input(f'Digite a {cores["lilas"]}primeira{cores["semestilo"]} nota: '))
n2 = float(input(f'Digite a {cores["verde"]}segunda{cores["semestilo"]} nota: '))
n3 = float(input(f'Digite a {cores["amarelo"]}terceira{cores["semestilo"]} nota: '))
n4 = float(input(f'Digite a {cores["vermelho"]}quarta{cores["semestilo"]} nota: '))
media = (n1+n2+n3+n4)/4
print(f'\nA média do aluno é igual a {cores["azul"]}{media:.1f}{cores["semestilo"]}')
print(f'{cores["azul"]}-'*67)
