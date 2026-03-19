print('<<< ola, vamos calcular o desconto do seu produto >>>')
valorI = float(input('Digite o valor do seu produto: ')) #I = inicial
descontoI = int(input('Dgite o valordo seu desconto: '))
descontoF = (valorI * descontoI) / 100 #F = Final
valorF = valorI - descontoF
print('O valor inicial foi de: R${} \nO valor do desconto foi de: R${}% \nE o valor a ser pago foi de: R${}'.format(valorI, descontoI, valorF))
