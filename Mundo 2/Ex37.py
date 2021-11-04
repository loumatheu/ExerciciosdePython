cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 37
===================================================================={cores['semestilo']}""")

print('                    CONVERSOR DE BASES NUMÉRICAS')

base = int(input(f"""\nPara qual base você deseja converter?
(1) Converter para {cores['verde']}binário{cores['semestilo']}
(2) Converter para {cores['azul']}octal{cores['semestilo']}
(3) Converter para {cores['amarelo']}hexadecimal{cores['semestilo']}

Digite 1, 2 ou 3: """))

numero = int(input('\nDigite um número inteiro: '))

if base == 1:
    print(f'{numero} convertido para binário é igual a {bin(numero)[2:]}.')
elif base == 2:
    print(f'{numero} convertido para binário é igual a {oct(numero)[2:]}.')
elif base == 3:
    print(f'{numero} convertido para binário é igual a {hex(numero)[2:]}.')
else:
    print('Opção inválida. Tente novamente.')
