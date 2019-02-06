print ('***** 11° Aula ******')

# Style = 0 (nenhum), 1(bold), 4(underline), 7(negative)

#text = 30 branco, 31 vermelho, 32verde, 33amarelo, 34azul, 35lilas, 36 azulpiscina, 37cinza

#back = 40branco, 41vermelho, 42verde, 43amarelo, 44azul, 45lilas, 46 azulpiscina, 47cinza

#para fazer a letra preta e a tela branca \33[7:30m

print('\033[4;35;40m----------- Oláaa Mundo -----------\033[m')

print('\033[7;30m Olá mundao\033[m')

a = 3
v = 5
print('Os valores são \033[32;45m{}\033[m  e \033[34;45m{}\033[m '.format(a, v))

nome = 'Andrezza'

print('Olá! Muito prazer em te conhecer, {}{}{} '.format('\033[33m',nome, '\033[m'))

cores = {'Limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m'}

print('Olá! tudo bem, {}{}{} '.format(cores['amarelo'], nome, cores['Limpa']))
