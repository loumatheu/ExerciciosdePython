import emoji

cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31', 'verde':'\033[1;32'}
print(f'{cores["azul"]}SIMULADOR DE EMPRÉSTIMO BANCÁRIO{cores["semestilo"]}')

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 36
===================================================================={cores['semestilo']}""")

nome = str(input('Qual o seu nome?')).strip()
print(f'Olá, Sr.{cores["azul"]}{nome}{cores["semestilo"]} é um prazer tê-lo em nosso sistema bancário!')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário atual? R$'))
tempo = int(input('Em quantos anos você deseja quitar o empréstimo?'))

pagamentomensal = (casa / tempo)/12

if pagamentomensal > (0.3 * salario):
    print(emoji.emojize(f'{cores["vermelho"]}Infelizmente{cores["semestilo"]}, o seu empréstimo não foi '
                        f'aprovado.:cry:', use_aliases=True))
else:
    print(emoji.emojize(f'{cores["azul"]}Parabéns! O seu empréstimo foi aprovado!:heart_eyes::heavy_dollar_sign:'
                        f'{cores["semestilo"]}', use_aliases=True))
    print(f'Caso opte por contratar o empréstimo em nosso banco, o(a) senhor(a) estará sujeito a tais obrigações:')
    print(f'Valor total do empréstimo: {cores["azul"]}R${casa:.2f}{cores["semestilo"]}')
    print(f'Valor a ser pago mensalmente: {cores["azul"]}R${pagamentomensal:.2f}{cores["semestilo"]}')
    if tempo == 1:
        print(f'Tempo limite de quitação do empréstimo: {cores["azul"]}{tempo} ano{cores["semestilo"]}')
    else:
        print(f'Tempo limite de quitação do empréstimo: {cores["azul"]}{tempo} anos{cores["semestilo"]}')

print(emoji.emojize(f'{cores["azul"]}Obrigado por procurar os serviços de nosso banco!:smiley:{cores["semestilo"]}'
                    f'', use_aliases=True))
