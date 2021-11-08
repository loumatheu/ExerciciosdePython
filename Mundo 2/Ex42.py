cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'branco':'\033[1;97m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 42
===================================================================={cores['semestilo']}""")

a = float(input('Insira o valor da primeira segmento: '))
b = float(input('Insira o valor da segunda segmento: '))
c = float(input('Insira o valor da terceira segmento: '))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    if a == b == c:
        print(f'É possível formar um {cores["branco"]}triângulo equilátero.{cores["semestilo"]}')
    elif a == b or b == c or a == c:
        print(f'É possível formar um {cores["verde"]}triângulo isósceles{cores["semestilo"]}.')
    else:
        print(f'É possível formar um {cores["vermelho"]}triângulo escaleno{cores["semestilo"]}.')
else:
    print(f'{cores["amarelo"]}Infelizmente não é possível formar um triângulo!{cores["semestilo"]}')
    print('Tente novamente!')

print('Reinicie o programa e verifique se é possível a existência de um triângulo!')
