
tempo = int(input('Quantos anos tem seu carro?'))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')

nome = str(input('Qual é seu nome?'))

if nome == 'Andrezza':
    print ('Que nome lindo você tem')
else:
    print('Seu nome é tao normal')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))

m = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Média ok')
else:
    print('Que média lixo')

