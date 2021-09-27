#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não forma um triângulo.
a = int(input('Insira o valor da primeira reta: '))
b = int(input('Insira o valor da segunda reta: '))
c = int(input('Insira o valor da terceira reta: '))

if (b - c) < a < (b + c):
    print('Sim! É possível formar um triângulo com as três retas!X')
else:
    if (a - c) < b < (a + c):
        print('Sim! É possível formar um triângulo com as três retas!Y')
    else:
        if (a - b) < c < (a + b):
            print('Sim! É possível formar um triângulo com as três retas!Z')
        else:
            print('Infelizmente não é possível formar um triângulo!')
            print('Tente novamente!')

print('Reinicie o programa e verifique se é possível a existência de um triângulo!')

Não funcionou