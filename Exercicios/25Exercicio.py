# leia o nome de uma pessoa e diga se ela tem silva no nome

nome = str(input('Informe o nome')).strip()

print('Seu nome é: {}'.format('silva' in nome.lower()))


