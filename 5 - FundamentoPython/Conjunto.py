# Criar um conjunto
Conjunto = {1, 2, 3}
print(Conjunto)
print(type(Conjunto))

# Conjunto[0] - não permite index

Conjunto_2 = set('coddddd 122')
print(Conjunto_2)

# Comparação entre conjuntos, ignora campos repetidos e a ordem dos itens
print({1, 2, 3} == {3, 2, 1, 3})


# Operações

# União de 2 conjuntos
c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))

# interseção de 2 conjuntos
c1 = {1, 2}
c2 = {2, 3}

print(c1.intersection(c2))

# subconjunto e superconjunto
print(c2 <= c1)
print(c2 >= c1)

# diferença entre conjuntos
print(c1 - c2)
