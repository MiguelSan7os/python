
# tabuada
from ast import For


numero = int(input("Digite um numero da taboada: "))

cont=0
while(cont<=10):
    print("{} X {} = {}".format(numero,cont,(cont*numero)))
    cont=cont+1



