# calcular preco com 5% de desconto


precoTotal = float(input("Digite o valor o item R$ "))
desconto = precoTotal*5/100
precoComDesconto = precoTotal-desconto

print('O preco do seu produto é R$ {:.2f} e com 5% de desconto fica R$ {:.2f}'.format(precoTotal, precoComDesconto))


