#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome separadamente.
#ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 27
===================================================================={cores['semestilo']}""")

nome = input('Qual o seu nome? ').strip()
lista = nome.split()
print(f'Prazer em conhecê-la(o)! \nO seu primeiro nome é {lista[0]} e o seu último nome é {lista[-1]}.')
