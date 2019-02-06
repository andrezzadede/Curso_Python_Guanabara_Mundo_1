#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não forma um triangulo.

r1 = float(input('Informe a primeira reta'))
r2 = float(input('Informe a segunda reta'))
r3 = float(input('Informe a terceira reta'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')