cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 09
===================================================================={cores['semestilo']}""")

print(f'{cores["vermelho"]}                              TABUADA{cores["semestilo"]}')
tab = int(input('Digite um número e descubra sua tabuada: '))
print('-'*67)
print(f'{cores["verde"]}{tab} x {1:2} = {tab*1}')
print(f'{tab} x {2:2} = {tab*2}')
print(f'{tab} x {3:2} = {tab*3}')
print(f'{tab} x {4:2} = {tab*4}')
print(f'{tab} x {5:2} = {tab*5}')
print(f'{tab} x {6:2} = {tab*6}')
print(f'{tab} x {7:2} = {tab*7}')
print(f'{tab} x {8:2} = {tab*8}')
print(f'{tab} x {9:2} = {tab*9}')
print(f'{tab} x 10 = {tab*10}{cores["semestilo"]}')
print(f'{cores["azul"]}-'*67)
#O :2 só formata o número e diz que ele tem duas casas decimais, sendo assim, a visualização fica mais bonita.
