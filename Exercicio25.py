import emoji
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Olá! Qual o seu nome? ')).strip()
if ('Silva' in nome):
    print(emoji.emojize('Você tem um belíssimo nome e ele possue a palavra Silva!:satisfied:', use_aliases=True))
else:
    print(emoji.emojize('Infelizmente o seu nome não tem Silva :cry:', use_aliases=True))
