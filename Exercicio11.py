print('CHALLENGE 11')
print('='*20, 'PAINT MESUAREMENT', '='*20)
print('Quantos litros de tinta eu preciso para pintar uma parede?')
print('-'*60)
b = float(input('Digite a largura da sua parede em metros: '))
h = float(input('Digite a altura da sua parede em metros: '))
tinta = (b*h)/2
a = (b*h)
print(f'A área da parede é de {a:.2f}m² e serão necessários aproximadamente {tinta:.1f}L de tinta para pintá-la completamente!')
print('-'*60)
