#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
year = int(input('Insira o ano: '))

if year % 4 == 0 and year % 100 != 0 or year % 4 == 0:
    print(f'O ano {year} é bissexto!')
else:
    print(f'O ano de {year} não é bissexto!')

print('Exute o programa novamente para consultar outro ano!')
