from random import choice
import emoji

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 19
===================================================================={cores['semestilo']}""")

print(emoji.emojize(':star::star::star::star: SORTEIO :star::star::star::star:', use_aliases=True))

print('Digite o número dos quatro alunos a serem sorteados para apagar o quadro.')
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]

print(f'O aluno que apagará o quadro será: {choice(alunos)}')
