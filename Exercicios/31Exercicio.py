#Desenvolva um programa que pergunte a distancia de uma viagem em KM
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas

d = float(input('Informe a distancia'))

if d <=200:
    preço = 0.50*d
else:
    preço = 0.45*d
print('O valor da sua passagem é {:.2f}'.format(preço))