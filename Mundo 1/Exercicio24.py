#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 24
===================================================================={cores['semestilo']}""")

cidade = str(input('Digite o nome de um cidade: ')).strip()

if (cidade[:5] == 'Santo'):
    print(f'A cidade de {cidade} começa com a palavra Santo em seu nome.')
else:
    print(f'O nome da sua cidade de {cidade} não começa com a palavra Santo.')
