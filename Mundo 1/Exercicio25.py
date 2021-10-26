import emoji

#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 25
===================================================================={cores['semestilo']}""")

nome = str(input('Olá! Qual o seu nome? ')).strip()
if ('Silva' in nome):
    print(emoji.emojize('Você tem um belíssimo nome e ele possue a palavra Silva!:satisfied:', use_aliases=True))
else:
    print(emoji.emojize('Infelizmente o seu nome não tem Silva :cry:', use_aliases=True))
