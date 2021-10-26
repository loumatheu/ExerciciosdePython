#Challenge 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#•O nome com todas as letras maiúsculas;
#•O nome com todas as letras minúsculas;
#•Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome;
cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 22
===================================================================={cores['semestilo']}""")

nome = str(input('Qual o seu nome completo? ')).strip()
print(f'Nome com todas as letras maiúsculas:{nome.upper()}')
print(f'Nome com letras minúsculas:{nome.lower()}')
print(f'Quantidade de letras que o nome possue:{len(nome.replace(" ", ""))} ')
firstname = nome.split()
print(f'Quantidade de letras do primeiro nome:{len(firstname[0])}')
