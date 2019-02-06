#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
#Digite um numero: 3.222, o numero 3.222 tem a parte inteira 3

from math import trunc
n = float (input('Informe um número:'))

print ('O número que você digitou é {}, sua parte inteira é {}'.format(n, trunc(n)))

# o math.trunc consegue pegar apenas a parte inteira do número

# Outra forma de fazer o mesmo exercicio

num = float (input('Informe um valor'))
print('O numero {}, tem seu valor inteiro de {}'.format(num, int(num)))