# calcular novo salario co 15% de aumento


salario = float(input("Digite o valor do seu salario antigo R$ "))
aumento = salario*15/100
salAumentando = salario+aumento

print('o seu Salario de R${:.2f} foi aumentado com 15% e agora ficou R${:.2f}'.format(salario, salAumentando))


