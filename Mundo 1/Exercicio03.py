cores = {'VermelhoBold':'\033[1;31m',
         'VerdeBold':'\033[1;32m',
         'AmareloBold':'\033[1;33m',
         'AzulBold':'\033[1;34m',
         'LilasBold':'\033[1;35m',
         'VerdepiscinaBold':'\33[1;36m',
         'CinzaBold':'\033[1;37m',
         'Semestilo':'\033[m',
         'FundoBranco':'\033[1;40m'}

print(f'{cores["FundoBranco"]}CHALLENGE 03{cores["Semestilo"]}')

n1 = int(input('Digite um número:'))
n2 = int(input("Digite outro número:"))
s = int(n1 + n2)
print("A soma entre {}{}{} e {}{}{} é igual a {}!".format(cores['VermelhoBold'], n1, cores['Semestilo'],
                                                                               cores['VerdeBold'], n2,
                                                                               cores['Semestilo'], s))
print(f'{cores["AzulBold"]}-'*67)
