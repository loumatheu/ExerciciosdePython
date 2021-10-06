#Challenge 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#•O nome com todas as letras maiúsculas;
#•O nome com todas as letras minúsculas;
#•Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome;
nome = str(input('Qual o seu nome completo? ')).strip()
print(f'Nome com todas as letras maiúsculas:{nome.upper()}')
print(f'Nome com letras minúsculas:{nome.lower()}')
print(f'Quantidade de letras que o nome possue:{len(nome.replace(" ", ""))} ')
firstname = nome.split()
print(f'Quantidade de letras do primeiro nome:{len(firstname[0])}')
