import emoji
cores = {'azul':'\033[1;34m','semestilo':'\033[m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 02
===================================================================={cores['semestilo']}""")


nome = input('Digite o seu nome:').strip()
print(emoji.emojize(f'É um prazer conhecê-lo(a), {nome}!:smiley:', use_aliases=True))
print(f'{cores["azul"]}-'*67)
