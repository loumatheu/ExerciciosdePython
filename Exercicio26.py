#Faça um programa que leia uma frase pelo teclado e mostre
# • Quantas vezes aparece a letra "A"
# • Em que posição ela aparece a primeira vez.
# • Em que posição ela paarece a última vez.
nome = input('Qual o seu nome? ').strip()


if 'a' in nome and 'A' in nome:
    print(f'A letra a aparece {(nome.upper().count("A"))} vezes no seu nome.')
    print(f'A letra "a" aparece primeiramente na posição {nome.lower().find("a")+1} e sua última posição é na posição '
          f'{nome.lower().rfind("a")+1}!')
else:
    print('Sinto muito, o seu nome não possui letra a.')
