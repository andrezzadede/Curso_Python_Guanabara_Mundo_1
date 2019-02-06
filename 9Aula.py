# Manipulando Texto

frase = str (input('informe o nome'))

print (frase[0:5]) #Vai mostrar apenas as letras do 0 ao 4

print (frase[2:]) #Aqui vai do 2 até o final

print (frase[2::6]) #Vai começar no nove, vai ate o final, mas ele vai pular de tres em tres

len(frase) #Vai mostrar quantos caracteres tem na frase

frase.count('o') #Contar quantas vezes aparece a letra o

frase.count('o', 0, 13) #Ele já fatia, vai do 0 até o 12 vendo nesse intervalo quantas letras o tem

frase.find('deo') #Quantas vezes ele encontro deo

frase.find('Android') #Se não tiver a palavra, ele te retorna -1, significaria que nao existe essa string

'Curso' in frase #dentro da frase existe essa palavra? Ele diz sim ou não, true or false

frase.replace('Python', 'Android') #Onde tem pyhton ele vai substituir por Android

frase.upper() #Ele vai por tudo em maiusculo e o que for em maiusculo continua em maiusculo

frase.lower()#Ele mantem o que é minusculo e substitui os maiusculos para minusculo

frase.capitalize() #Ele joga tudo para minusculo e só o primeiro vai ficar em maiusculo

frase.title() #Ele vai deixar em maiusculo a primeira letra de todas as palavras

frase.strip() #Ele remove espaços inuteis no inicio e no fim

frase.rstrip() #Ele remove apenas os ultimos espaços

frase.lstrip() #Ele remove os espaços do começo da frase

frase.split() #Ele divide dentro da string, ou seja, onde está o espaço, ele divide a palavra e faz uma nova lista com novos indices

'-'.join(frase) #Ele vai colocar um tracinho nos espaços vagos

print("""A agua do mar estava agitada, caminhamos em direção à praia, nossos pés tocando a areia de uma forma tão humana, mas ao mesmo tempo tão sobrenatural. Ou talvez não, por ser algo tão gostoso e por me fazer me lembra de minhas vidas passadas a sensação dos grãos de areia em contato com minha pele me assustava. 
Um trovão soou alto e foi possível ver um raio surgir no céu, em seguida os pingos de chuva caíram sobre nós. Olhei para cima, essa era uma resposta dele? Por sermos criaturas demoníacas ele estava tirando o melhor de nós? Por sermos sugadores de sangue? Era esse o nosso castigo? 
""")

print(frase.upper().count('o')) #Se voce quiser saber quantos O tem maiusculo e minusculo




