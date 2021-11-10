cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'branco':'\033[1;97m', 'ciano':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 45
===================================================================={cores['semestilo']}""")

print(' '*20, f'{cores["azul"]}NÚMEROS PARES DE 1 - 50{cores["branco"]}')
for c in range(0, 52, 2):
    print(c, ' ', end='')