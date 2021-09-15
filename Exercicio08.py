print('CHALLENGE 08')
print('='*5, 'CONVERSOR DE MEDIDAS', '='*5)
m = float(input('Digite um valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dcm = m*10
cm = m*100
mm = m*1000
print(f'Conversão da medida: \n Quilômetro = {km}km \n Hectômetro = {hm}hm \n Decâmetro = {dam}dam \n Metro = {m}m', end='')
print(f'\n Decimetro {dcm}dcm \n Centímetro {cm}cm \n Milímetro {mm}mm')
#O outro print sendo usado tradicionalmente seria mais bonito, optei por utilizar o \n para não esquecer.
