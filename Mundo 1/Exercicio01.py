import emoji
cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 01
===================================================================={cores['semestilo']}""")

mensagem = emoji.emojize(f'{cores["verde"]}Hello, World!:earth_americas:{cores["semestilo"]}', use_aliases=True)
print(mensagem)
print(f'{cores["azul"]}-'*67)
