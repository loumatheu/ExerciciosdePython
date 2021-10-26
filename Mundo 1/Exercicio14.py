cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 14
===================================================================={cores['semestilo']}""")

print(f'{cores["azul"]}                     Conversor de Temperatura')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
C = float(input('Informe uma temperatura em ºC: '))
F = (C*9/5)+32
print(f'{cores["lilas"]}{C}ºC{cores["semestilo"]} corresponde a {cores["amarelo"]}{F}ºF{cores["semestilo"]}. ')
if C <= 15:
    print(f'{cores["azul"]}Está congelando!')
elif C >= 27:
    print(f'{cores["vermelho"]}Está pegando fogo!')
else:
    print(f'{cores["verde"]}A temperatura está agradável!')
print(f'{cores["azul"]}-{cores["semestilo"]}'*67)
