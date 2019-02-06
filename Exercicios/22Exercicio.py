# Crie um programa que leia o nome completo de uma pessoa e mostre
# A- Nome com todas as letras maiusculas
# B- O nome com todas as letras minusculas
# C- Quantas letras ao todo(sem consideraças espaços)
# D- Quantas letras tem o primeiro nome

nome = str(input('Informe seu nome completo')).strip()

print(nome.upper())

print(  nome.lower())

print(len(nome) - nome.count(' '))

print(nome.find(' '))

separa = nome.split()
print(len(separa[0]))
