#Faça um programa que leia uma frase pelo teclado e mostre
# • Quantas vezes aparece a letra "A"
# • Em que posição ela aparece a primeira vez.
# • Em que posição ela paarece a última vez.

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 26
===================================================================={cores['semestilo']}""")

nome = input('Qual o seu nome? ').strip()

if 'a' in nome and 'A' in nome:
    print(f'A letra a aparece {(nome.upper().count("A"))} vezes no seu nome.')
    print(f'A letra "a" aparece primeiramente na posição {nome.lower().find("a")+1} e sua última posição é na posição '
          f'{nome.lower().rfind("a")+1}!')
else:
    print('Sinto muito, o seu nome não possui letra a.')
