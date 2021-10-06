#Crie um programa que leia um número inteiro qualquer e mostre na tela se le é PAR ou IMPAR.
n = float(input('Digite um número: '))
resto = n % 2


if resto == 0:
    print(f'O número {n:.0f} é par!')
else:
    print(f'O número {n:.0f} é impar!')

print('Reinicie o programa e digite outro número!')