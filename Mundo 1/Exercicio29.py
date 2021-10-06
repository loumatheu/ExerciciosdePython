#Escreva um programa que leia velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7 para cada km acima do limite.
print("""===========================================================================================================
                                   CALCULADOR E IDENTIFICADOR DE MULTAS
===========================================================================================================""")
v = int(input('Insira a velocidade do veículo: '))

if v > 80:
    multa = (v - 80) * 7
    print(f'Você ultrapassou o limite de velocidade pré-definido. Sua penalidade é uma multa de R${multa}!')
else:
    print('O motorista está dirigindo conforme a lesgilação vigente!')

print('Dirija com cuidado e sempre obedeça a lesgilação!')
