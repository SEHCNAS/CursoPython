generator = (i ** 2 for i in range(10) if i % 2 == 0)
# Gera os itens do generator
for numero in generator:
    print(numero)
