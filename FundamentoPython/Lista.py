Lista = []
# Tamanho da lista
print(len(Lista))

# Adicionar itens na lista
Lista.append(0)
Lista.append(5)
print(Lista)
print(len(Lista))

Lista_2 = ['texto', 1, 'texto_2', 2]
print(Lista_2)


# Remover item da lista
Lista_2.remove(1)
print(Lista_2)

# Reverter uma lista
Lista_2.reverse()
print(Lista_2)

# Acessar o index de um objeto dentro da lista
Lista_3 = [1, 5, 'Gabriel', 'Sanches', 3.1415]
print(Lista_3.index('Gabriel'))

# Validar se item esta na lista
print(1 in Lista_3)
print('Gabriel' in Lista_3)
