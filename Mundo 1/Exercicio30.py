#Crie um programa que leia um número inteiro qualquer e mostre na tela se le é PAR ou IMPAR.
print(f"""{cores['azul']}====================================================================
                            CHALLENGE 30
===================================================================={cores['semestilo']}""")

n = float(input('Digite um número: '))
resto = n % 2


if resto == 0:
    print(f'O número {n:.0f} é par!')
else:
    print(f'O número {n:.0f} é impar!')

print('Reinicie o programa e digite outro número!')