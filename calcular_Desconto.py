print('<<< ola, vamos calcular o seu descontro >>>')
valorI = float(input('Digite o valor do seu produto: '))
descontoI = int(input('Dgite o valordo seu desconto: '))
descontoF = (valorI * descontoI) / 100
valorF = valorI - descontoF
print('O valor inicial foi de: R${} \nO valor do desconto foi de: R${}% \nE o valor a ser pago foi de: R${}'.format(valorI, descontoI, valorF))
