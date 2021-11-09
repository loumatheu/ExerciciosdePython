import emoji
cores = {'azul':'\033[1;34m', 'semestilo':'\033[m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 44
===================================================================={cores['semestilo']}""")

print(f'                    {cores["azul"]}GERENCIAMENTO DE PAGAMENTO{cores["semestilo"]}')

compras = float(input('Preço das compras R$: '))

pagamento = int(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Digite uma opção: """))

if pagamento == 1:
    valorapagar = compras * 90/100
    print(f'Total= R${compras:.2f}      Total a pagar= R${valorapagar:.2f}')
elif pagamento == 2:
    valorapagar = compras * 95/100
    print(f'Total= R${compras:.2f}      Total a pagar= R${valorapagar:.2f}')
elif pagamento == 3:
    parcelas = compras / 2
    print(f'Total= R${compras:.2f}      Total a pagar= R${compras:.2f}      Parcelas= 2x R${parcelas:.2f}')
elif pagamento == 4:
    divisoes = int(input('Digite quantas vezes você quer dividir: '))
    valorapagar = (compras * 120/100)
    parcelas = valorapagar / divisoes
    print(f'Total= R${compras:.2f}      Total a pagar= R${valorapagar:.2f}      Parcelas= {divisoes}x R${parcelas:.2f}')
else:
    print('Opção indisponível, tente novamente.')

print(emoji.emojize('Obrigado pela preferência, volte sempre!:satisfied::blue_heart:', use_aliases=True))
