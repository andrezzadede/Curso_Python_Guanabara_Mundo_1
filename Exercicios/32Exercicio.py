# Faça um programa que leia um ano qualquer e ve se é um ano bissexto
from datetime import date
ano = int(input('Informe o ano ou coloque zero se quer que pegue o ano atual'))

if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 !=0 or ano % 400 ==0:
    print('Ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))