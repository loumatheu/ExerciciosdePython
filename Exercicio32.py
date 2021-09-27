#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
year = int(input('Insira o ano: '))
biyear = year % 4

if biyear == 0:
    print(f'O ano {year} é bissexto!')
else:
    print(f'O ano de {year} não é bissexto!')

print('Exute o programa novamente para consultar outro ano!')
