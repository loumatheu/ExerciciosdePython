from math import pow
cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'branco':'\033[1;97m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 43
===================================================================={cores['semestilo']}""")

print(f'{cores["azul"]}                IMC - Índice de Massa Corpórea{cores["semestilo"]}')
altura = float(input('Altura (m): '))
peso = float(input('Peso (Kg): '))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print(f'{cores["branco"]}O seu IMC é {imc:.1f} e você está ABAIXO DO PESO.{cores["semestilo"]}')
elif 18.5 < imc <= 24.9:
    print(f'{cores["branco"]}O seu IMC é {imc:.1f} e você está com o PESO IDEAL.{cores["semestilo"]}')
elif 24.9 < imc <= 30:
    print(f'{cores["branco"]}O seu IMC é {imc:.1f} e você está ACIMA DO PESO.{cores["semestilo"]}')
elif 30 < imc <= 40:
    print(f'{cores["branco"]}O seu IMC é {imc:.1f} e você está com OBESIDADE.{cores["semestilo"]}')
elif imc >= 40:
    print(f'{cores["branco"]}O seu IMC é {imc:.1f} e você está com OBESIDADE MÓRBIDA.{cores["semestilo"]}')

print(f'{cores["azul"]}Coma alimentos saudáveis e pratique exercícios!{cores["semestilo"]}')
