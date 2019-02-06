# 11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
# e a quantidade de tinta necessaria para pinta-la. sabendo que cada litro de tinta pinta uma area de 2m2

larg = float(input('Largura da parede'))

alt = float(input('Altura da parede:'))

area = larg * alt

print ('Essa é a area em {}m2'.format(larg, alt, area))

tinta = area/2
print ('Para pintar a parede é necessario', tinta)