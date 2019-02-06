# Adição = +
# Subtração = -
# Multiplicação = *
# Divisão = /
# Potencia = **
# Divisão inteira = //
# Resto da Divisão = %


# Ordem de precedencias

# 1 = ()
# 2 = **
# 3 = * / // % = Faz quem aparecer primeiro
# 4 = + -

nome = input ('Qual é seu nome? ')

print ('Prazer em te conhecer {}!'.format(nome))

n1 = int (input('Informe um valor: '))
n2 = int (input('Informe outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, o produto é {}, \n e a divisão é {}'.format(s, m, d), end=' ')
print ('Divisão inteira é  {} e potencia {}'.format(di, e))

# end='' continua naa mesma linha o print
# \n pula a linha do print

