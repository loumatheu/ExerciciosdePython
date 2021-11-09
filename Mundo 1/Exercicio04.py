cores = {'AzulBold':'\033[1;34m', 'BlueBack':'\033[1;44m', 'Semestilo':'\033[m'}

print(f'{cores["AzulBold"]}==============================================={cores["Semestilo"]}')
print(f'{cores["AzulBold"]}                 CHALLENGE 04{cores["Semestilo"]}')
print(f'{cores["AzulBold"]}==============================================={cores["Semestilo"]}')

var = input('Digite um valor qualquer:')
print('Sua variável é do tipo:', type(var))
print('Sua váriável é um espaço?', var.isspace())
print('Sua variável é alfanumérica?', var.isalnum())
print('Sua variável é um número?', var.isnumeric())
print('Sua variável é imrpimível?', var.isprintable())
print('Sua variável é letra?', var.isalpha())
print('Sua variável está capitalizada(com letras maiúsculas)?', var.istitle())
print(f'{cores["AzulBold"]}-'*67)
