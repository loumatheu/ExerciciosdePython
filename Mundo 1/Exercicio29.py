#Escreva um programa que leia velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7 para cada km acima do limite.
cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 29
===================================================================={cores['semestilo']}""")

print(f"""{cores['vermelho']}====================================================================
                 CALCULADOR E IDENTIFICADOR DE MULTAS
===================================================================={cores['semestilo']}""")
v = int(input('Insira a velocidade do veículo: '))

if v > 80:
    multa = (v - 80) * 7
    print(f'{cores["vermelho"]}Você ultrapassou o limite de velocidade pré-definido.'
          f'Sua penalidade é uma multa de R${multa}!{cores["semestilo"]}')
else:
    print(f'{cores["verde"]}O motorista está dirigindo conforme a lesgilação vigente!{cores["semestilo"]}')

print(f'{cores["amarelo"]}Dirija com cuidado e sempre obedeça a lesgilação!')
