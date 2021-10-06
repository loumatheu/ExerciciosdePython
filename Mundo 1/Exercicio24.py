#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome de um cidade: ')).strip()

if (cidade[:5] == 'Santo'):
    print(f'A cidade de {cidade} começa com a palavra Santo em seu nome.')
else:
    print(f'O nome da sua cidade de {cidade} não começa com a palavra Santo.')
