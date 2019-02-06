#Faça um programa que leia um angulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input('Informe o angulo por favor:'))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print ('O Seno, cosseno e tangente desse {} angulo são esses {:.2f}, {:.2f}, {:.2f} sucessivamente'.format(angulo, seno, cosseno, tangente))