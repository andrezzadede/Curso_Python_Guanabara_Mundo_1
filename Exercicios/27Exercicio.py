# Faça um programa que leia o nome completo da pessoa e mostre o primeiro e o ultimo ano da menina
#Exemplo primeiro=Ana, ultimo=Souza

nome = str(input('Informe o nome')).strip()

dividir = nome.split()

nome1 = dividir[0]

nome2 = dividir[len(dividir)-1]

print('O primeiro nome é {} e o ultimo é {}'.format(nome1, nome2))

