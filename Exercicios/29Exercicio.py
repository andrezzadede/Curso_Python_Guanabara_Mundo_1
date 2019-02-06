#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80k emita uma mensagem dizendo que foi multado.
#Calcule a multa vai custar 7 reais por km

vec = int(input('Informe a velocidade do carro'))

if vec > 80:
    print('Sua velocidade está maior do que deveria')
    multa = (vec-80)*7
    print('O preço da sua multa é de {}'.format(multa))
else:
    print('Parabéns, você está dentro dos limites de velocidade!')
