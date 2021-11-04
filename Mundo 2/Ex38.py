cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m'}
print(f'{cores["azul"]}SIMULADOR DE EMPRÉSTIMO BANCÁRIO{cores["semestilo"]}')

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 38
===================================================================={cores['semestilo']}""")

print(f'                       {cores["azul"]}QUAL NÚMERO É MAIOR?{cores["semestilo"]}')
n1 = int(input('\nDigite um número inteiro: '))
n2 = int(input('Digite outro número inteiro:'))

if n1 > n2:
    print(f'{cores["verde"]}{n1}{cores["semestilo"]} é maior que {cores["azul"]}{n2}{cores["semestilo"]}.')
elif n2 > n1:
    print(f'{cores["verde"]}{n2}{cores["semestilo"]} é maior que {cores["azul"]}{n1}{cores["semestilo"]}.')
else:
    print(f'{cores["vermelho"]}Não existe{cores["semestilo"]} valor maior, pois os dois números são {cores["azul"]}'
          f'iguais{cores["semestilo"]}.')
