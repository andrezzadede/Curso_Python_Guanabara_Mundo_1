# Faça um programa que leia uma frase e mostre
# Quantas vezes aparece a letra A,
# em que posição ela aparece a primeira vez e
# em que posição ela aparece na ultima vezes

frase = str(input('Informe a frase')).strip()

frase = frase.lower()

print('A quantidade de a é {} '.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A ultima letra A apareceu em {}'.format(frase.rfind('a')+1))