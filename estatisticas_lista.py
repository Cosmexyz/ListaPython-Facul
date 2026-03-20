num1 = float(input('Digite o PRIMEIRO número: '))
num2 = float(input('Digite o SEGUNDO número: '))
num3 = float(input('Digite o TERCEIRO número: '))
num4 = float(input('Digite o QUARTO número: '))
num5 = float(input('Digite o QUINTO número: '))

lista = [num1, num2, num3, num4, num5]

def atributos(lista):
    maior = max(lista)
    menor = min(lista) 
    soma = sum(lista)

    return maior, menor, soma

maior, menor, soma = atributos(lista)

print('Maior:', maior)
print('Menor:', menor)
print('Soma: ', soma)


