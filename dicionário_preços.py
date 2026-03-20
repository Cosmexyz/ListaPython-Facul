busca = input('Ola, temos: Coca-cola, Sprit, Fanta ou Água. Qual vai querer?\n')

produtos = {
    'coca' : 4.50,
    'sprit': 3.90,
    'fanta': 4.0,
    'agua' : 1.50
}

if busca in produtos:
     print('Preço: R$',produtos[busca] )
else:
     print('Não encontrado')

    
 
    