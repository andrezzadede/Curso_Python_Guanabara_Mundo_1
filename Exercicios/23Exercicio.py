#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

#Exe: Digite um numero: 1834

#unidade: 4 # dezena:3 centena:8 milhar: 1

n = int(input('Informe o número'))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10


print('Analisando o numero {}'.format(n))

print('O milhar é {}, a centena é {}, a dezena é {} e a unidade é {}'.format(m, c, d, u))

