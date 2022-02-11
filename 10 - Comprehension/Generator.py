generator = (i ** 2 for i in range(10) if i % 2 == 0)
# Gera os itens de acordo com a chamada do next
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# se for chamado maior que o numnero de itens da erro
print(next(generator))
