#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome separadamente.
#ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = input('Qual o seu nome? ').strip()
lista = nome.split()
print(f'Prazer em conhecê-la(o)! \nO seu primeiro nome é {lista[0]} e o seu último nome é {lista[-1]}.')
