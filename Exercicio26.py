#Faça um programa que leia uma frase pelo teclado e mostre
# • Quantas vezes aparece a letra "A"
# • Em que posição ela aparece a primeira vez.
# • Em que posição ela paarece a última vez.
nome = input('Qual o seu nome? ')


if nome.find('a') and nome.find('A'):
    print('A letra a aparece {} vezes no seu nome.'.format(nome.count('a') + nome.count('A')))
    print(f'As letras a aparecem nas posições: {nome}')
else:
    print('Sinto muito, o seu nome não possui letra a.')

Não sei...