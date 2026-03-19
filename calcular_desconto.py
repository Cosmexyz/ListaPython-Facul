salario = float(input('Digite seu salario: R$'))
desconto = salario - (15 * salario ) / 100
print('Seu salario total é de R${} \nE após o desconto ficará: R${}'.format(salario, desconto))