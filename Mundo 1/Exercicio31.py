#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
#por km para viagens de até 200km e R$0,45 para viagens mais longas.
print(f"""{cores['azul']}====================================================================
                            CHALLENGE 31
===================================================================={cores['semestilo']}""")

distance = int(input('Insira a distância a ser percorrida em Km: '))

if distance <= 200:
    payment = distance * 0.5
    print(f'Em uma distância de {distance}Km o valor a ser pago é: R${payment}')
else:
    payment = distance * 0.45
    print(f'Em uma distância de {distance}Km valor a ser pago é: R${payment}')

print('Obrigado por utilizar o nosso calculador de passagens!')
