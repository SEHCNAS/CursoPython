from functools import reduce
from operator import add

valores = (30,10,25,71,100,94)

#sort na lista sem alterar a lista original
print(sorted(valores))
print(valores)

#Pega o menor valor sem alterar a lista
print(min(valores))

#Pega o maior valor sem alterar a lista
print(max(valores))

#soma os valores sem alterar a lista
print(sum(valores))
print(reduce(add, valores))

#revert sem alterar a lista
print(tuple(reversed(valores)))

#Sort mudando a lista original
#valores.sort()
#print(valores)


