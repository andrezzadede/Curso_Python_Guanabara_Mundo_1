# Faça um programa onde leia o nome de todos os alunos e sorteie um para apagar a lousa escrevendo o nome do individo
from random import choice
n1 = str (input('Informe o nome do aluno'))

n2 = str (input('Informe o nome do segundo aluno'))

n3 = str (input('Informe o nome do terceiro aluno'))

n4 = str (input('Informe o nome do quarto aluno'))

lista = [n1, n2, n3, n4]

escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))