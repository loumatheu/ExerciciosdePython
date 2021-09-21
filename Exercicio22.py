#Challenge 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#•O nome com todas as letras maiúsculas;
#•O nome com todas as letras minúsculas;
#•Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome;
nome = input('Qual o seu nome completo? ')
print('Nome com todas as letras maiúsculas: ')
print(nome.upper())
print('Nome com letras minúsculas:')
print(nome.lower())
print('Quantidade de letras que o nome possue: ')
print(nome.count)
print('Quantidade de letras do primeiro nome:')
firstname = nome.split()
print(firstname[1].count)
