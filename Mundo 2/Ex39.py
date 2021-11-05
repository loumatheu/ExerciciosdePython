from datetime import date

cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 39
===================================================================={cores['semestilo']}""")

print('                        ALISTAMENTO MILITAR')

nome = input('Insira seu nome: ').strip()
anodenascimento = int(input('Insira seu ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - anodenascimento

if idade < 18:
    alistamento = (18 - idade) + 2021
    print(f'Saudações, {nome}. Você tem {idade} anos e deverá se apresentar em {alistamento} nas forças armadas.')
elif idade == 18:
    print(f'Saudações, {nome}. Você tem {idade} anos e deve se apresentar IMEDIATAMENTE nas forças armadas.')
else:
    print(f'Saudações, {nome}. Você já deveria ter se alistado há {((idade - 18) - 2021) + 2021} anos!')
