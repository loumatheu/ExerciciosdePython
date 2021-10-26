#Challenge 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 23
===================================================================={cores['semestilo']}""")

num = int(input('Digite um número entre 0 e 9999: '))
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
