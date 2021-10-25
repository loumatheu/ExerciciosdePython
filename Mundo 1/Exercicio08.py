cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 08
===================================================================={cores['semestilo']}""")

print(f'                       {cores["verde"]}CONVERSOR DE MEDIDAS{cores["semestilo"]}')
m = float(input('Digite um valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dcm = m*10
cm = m*100
mm = m*1000
print(f'Conversão da medida:'
      f' \n {cores["vermelho"]}Quilômetro = {km}km{cores["semestilo"]} \n {cores["amarelo"]}Hectômetro = {hm}hm'
      f'{cores["semestilo"]} \n {cores["verde"]}Decâmetro = {dam}dam{cores["semestilo"]} '
      f'\n {cores["lilas"]}Metro = {m}m{cores["semestilo"]}', end='')
print(f'\n {cores["azul"]}Decimetro {dcm}dcm{cores["semestilo"]} '
      f'\n {cores["verdepiscina"]}Centímetro {cm}cm{cores["semestilo"]} \n Milímetro {mm}mm')
print(f'{cores["azul"]}-'*67)
#O outro print sendo usado tradicionalmente seria mais bonito, optei por utilizar o \n para não esquecer.
