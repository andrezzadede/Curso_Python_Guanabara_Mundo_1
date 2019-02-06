# 12 Faça um algoritmo que leia o preço de um produto e mostre o novo preço com 5% de desconto

preço = float (input('Qual é o preço do produto? RS'))
novo = preço - (preço*5/100)

input('O novo preço é R${}'.format(novo))


