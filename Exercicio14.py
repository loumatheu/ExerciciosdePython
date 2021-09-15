print('                  CHALLENGE 14')
print('='*11, 'Conversor de Temperatura', '='*11)
print('-'*50)
C = float(input('Informe uma temperatura em ºC: '))
F = (C*9/5)+32
print(f'{C}ºC corresponde a {F}ºF. ')
if C <= 15:
    print('Está congelando!')
elif C >= 27:
    print('Está pegando fogo!')
else:
    print('A temperatura está agradável!')
print('-'*50)
