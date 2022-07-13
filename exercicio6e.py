# calcular qtos dollar tem na carteira
#preco do dollar

numero = float(input("Quantos de dinheiro voce tem na carteira: "))
dollar = 3.27

convertDolar = float(numero/dollar)

print("Seus R${} na carteira vale {:.2f} dollar!".format(numero,convertDolar))



