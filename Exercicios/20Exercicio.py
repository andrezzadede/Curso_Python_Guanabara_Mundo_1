#Faça um programa que leia o nome de todos os alunos e faça uma ordem de quem vai apresentar os trabalhos
from random import shuffle
n1 = str(input ("Informe o primeiro nome"))
n2 = str(input("Informe o segundo nome"))
n3 = str(input("Informe o terceiro nome"))
n4 = str(input("Informe o quarto nome"))

lista = [n1, n2, n3, n4]

shuffle(lista)

print('A ordem de apresentação serta')
print(lista)