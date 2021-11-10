cores = {'azul':'\033[1;34m', 'semestilo':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m',
         'amarelo':'\033[1;33m', 'branco':'\033[1;97m', 'ciano':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 48
===================================================================={cores['semestilo']}""")

print(' '*20, f'{cores["azul"]}NÚMEROS MÚLTIPLOS DE 3 DE 1 - 500{cores["branco"]}')

for c in range(0, 500, 3):
        print(c)
