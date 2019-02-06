
n1 = int (input ('Digite um numero:'))
n2 = int (input ('Digite mais um numero:'))

s = n1 + n2

print ('A soma vale', s)

print ('A soma vale {}'.format(s))

print (type(n1))

print ('A soma entre', n1, 'e', n2, 'é', s )

print ('A soma entre {} e {} vale {}'.format(n1, n2, s))

# Se eu quiser converter o numero

n = float(input('Informe o numero'))
print (n)

# tipos str (string), float, bool or int

m = input ('digite algo')
print (m.isnumeric()) # para ver se é numerico

v = input ('digite algo')
t = input ('digite algo') # para ver se é um numero alfanumerico ou seja == 38d
print (t.isalnum())


