#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

co = float(input('Cateto oposto'))
ca = float(input('Cateto adjacente'))

hi = (co ** 2 + ca **2) ** (1/2)

print('Hipotenusa é {:.2f}'.format(hi))

#Outra solução

from math import hypot

h = hypot(co,ca)

print('Hipo é{:.2f} '.format(h))