#Crie um programa que leia o nome de uma cidade e diga se a sua cidade
# começa ou não com a palavra santo

cidade = str(input('Informe o nome da cidade'))

print(cidade[:5].upper() == 'Santo')
