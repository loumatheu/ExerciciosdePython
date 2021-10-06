#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 > n3:
    print(f'\nO maior número é {n1} e o menor número é {n3}!')
else:
    if n1 > n3 > n2:
        print(f'\nO maior número é {n1} e o menor número é {n2}!')
    else:
        if n2 > n1 > n3:
            print(f'\nO maior número é {n2} e o menor número é {n3}!')
        else:
            if n2 > n3 > n1:
                print(f'\nO maior número é {n2} e o menor número é {n1}!')
            else:
                if n3 > n2 > n1:
                    print(f'\nO maior número é {n3} e o menor número é {n1}!')
                else:
                    print(f'\nO maior número é {n3} e o menor número é {n2}!')

print('\nExecute o programa novamente e insira outros números!')
