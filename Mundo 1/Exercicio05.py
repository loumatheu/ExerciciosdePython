cores = {'Azulbold':'\033[1;34m','Verdebold':'\033[1;32m','Semestilo':'\033[m', 'VermelhoBold':'\033[1;31m',
         'Lilasbold':'\033[1;35m'}

print(f"""{cores['Azulbold']}====================================================================
                            CHALLENGE 05
===================================================================={cores['Semestilo']}""")

print('Descubra qual o antecessor e sucessor do número desejado!')
num = int(input('Escreva um valor numérico: '))
print(f'O sucessor de {cores["Verdebold"]}{num}{cores["Semestilo"]} é {cores["Lilasbold"]}{num+1}{cores["Semestilo"]} '
      f'e seu antecessor é {cores["VermelhoBold"]}{num-1}{cores["Semestilo"]}.')
print(f'{cores["Azulbold"]}-'*67)
