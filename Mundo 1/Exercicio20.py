from random import shuffle
from emoji import emojize

cores = {'azul':'\033[1;34m','verde':'\033[1;32m','semestilo':'\033[m', 'vermelho':'\033[1;31m',
         'lilas':'\033[1;35m', 'amarelo':'\033[1;33m', 'verdepiscina':'\033[1;36m'}

print(f"""{cores['azul']}====================================================================
                            CHALLENGE 20
===================================================================={cores['semestilo']}""")

print(emojize(':star: SORTEIO DE TRABALHOS A SEREM APRESENTADOS :star:', use_aliases=True))

print('Digite o nome dos quatro alunos a seguir e obtenha a ordem a de apresentação.')
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]
shuffle(alunos)

print(f'\nOs trabalhos serão apresentados na seguinte ordem: {alunos}')
