# Desafios!!



# 04 Faça um programa que leia algo pelo teclado mostre na tela o
# seu tipo primitivo e todas suas informaçoes possiveis sobre eles

po = input ('Digite algo por favor: ')
print (po.isalpha(), 'Ele é letra?', po.isalnum(), 'é alfanumerico?')
print ('O tipo é primitivo? ', type(po))
print ('Só tem espaços? ', po.isspace())
print ('É um numero? ', po.isnumeric())
print ('É alfabetico? ', po.isalpha())
print ('É alfanumerrico? ', po.isalnum())
print ('Está em maiscula? ', po.isupper())
print ('Está em minuscula? ', po.islower())
print ('Ele está captalizado? ', po.istitle())