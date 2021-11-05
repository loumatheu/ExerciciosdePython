cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 40
===================================================================={cores['semestilo']}""")

print(f'                         {cores["azul"]}CÁLCULO DE MÉDIA{cores["semestilo"]}')

nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1 + n2 + n3 + n4)/4

if media < 5.0:
    print(f'{nome} obteve media {media:.1f} e está {cores["vermelho"]}REPROVADO{cores["semestilo"]}.')
elif media <= 6.9:
    print(f'{nome} obete média {media:.1f} e está em {cores["amarelo"]}RECUPERAÇÃO{cores["semestilo"]}.')
else:
    print(f'{nome} obteve média {media:.1f} e foi {cores["azul"]}APROVADO!{cores["semestilo"]}')
