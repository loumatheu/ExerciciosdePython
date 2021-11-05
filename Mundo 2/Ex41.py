from datetime import date

cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'branco':'\033[1;97m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 41
===================================================================={cores['semestilo']}""")

print(f'        {cores["azul"]}CONFEDERAÇÃO BRASILEIRA DE DESPORTOS AQUÁTICOS - CDBA')
print(f'                             CADASTRO{cores["semestilo"]}')

nome = input('Nome: ').strip()
anodenascimento = int(input('Ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - anodenascimento

print(f'Atleta: {cores["verde"]}{nome}{cores["semestilo"]}      Idade:{cores["verde"]}{idade}{cores["semestilo"]}')

if idade <= 9:
    print(f'Sua categoria: {cores["azul"]}MIRIM{cores["semestilo"]}')
elif idade <= 14:
    print(f'Sua categoria: {cores["verde"]}INFANTIL{cores["semestilo"]}')
elif idade <= 19:
    print(f'Sua categoria: {cores["amarelo"]}JÚNIOR{cores["semestilo"]}')
elif idade <= 25:
    print(f'Sua categoria: {cores["vermelho"]}SÊNIOR{cores["semestilo"]}')
else:
    print(f'Sua categoria: {cores["lilas"]}MASTER{cores["semestilo"]}')
