#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não forma um triângulo.
print(f"""{cores['azul']}====================================================================
                            CHALLENGE 35
===================================================================={cores['semestilo']}""")

a = float(input('Insira o valor da primeira segmento: '))
b = float(input('Insira o valor da segunda segmento: '))
c = float(input('Insira o valor da terceira segmento: '))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print('Sim! É possível formar um triângulo com as três retas!')
else:
    print('Infelizmente não é possível formar um triângulo!')
    print('Tente novamente!')

print('Reinicie o programa e verifique se é possível a existência de um triângulo!')
