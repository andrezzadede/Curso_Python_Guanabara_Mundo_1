#Faça um programa que leia tres numeros e veja qual é o maior e o menor

a = float(input('Informe o numero'))
b = float(input('Informe o numero 2'))
c = float (input('Informe o numero 3'))

maior = a;
menor = a;

if b < a and b < c:
    menor = b
if c < a and c < b:
        menor = c
print('O maior número é {} '.format(menor))

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {} '.format(maior))

