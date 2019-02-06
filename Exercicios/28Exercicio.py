#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuario venceu ou perdes

from random import randint

v = int(input('Informe um número de 0 a cinco'))

g = randint(0,5)

if v == g:
    print('Acertou! {}'.format(g))
else:
    print('O pc venceu{}'.format(g))



