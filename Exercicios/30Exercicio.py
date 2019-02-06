#Crie um programa que veja se o numero é par ou impar

n = int (input('Informe o número'))

resultado = n % 2 # & Ele pode ser usado para ver se é impar ou par

if resultado == 1:
    print('O número {} é impar'.format(n))
else:
    print('O número {} é par'.format(n))