#Calcule o salario do funcionario e calcule o aumento
#Para salarios superiores a R$1.250,00 calcule um aumento de 10%
#Para os inferior ou iguais, o aumento é de 15%

salario = float(input('Por favor, informe seu salário R$'))

if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario *10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora '.format(salario, novo))

print('Tenha um bom dia!')