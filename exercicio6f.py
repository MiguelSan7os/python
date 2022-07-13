# calcular qtdade de tinta para pintar uma parede em m2


altura = float(input("Digite a altura da parede:"))
largura = float(input("Digite a largura da parede:"))
metragem = altura*largura
qtdTinta = metragem/2

print("A altura é {}m e largura é {}m a metragem total é {}m e foi gasto {}lt de tinta".format(altura, largura, metragem, qtdTinta))


