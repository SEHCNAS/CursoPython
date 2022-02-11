from string import Template

Nome, Idade = 'Gabriel', 22

# Fazendo a interpolação da forma antiga
print('Nome %s, idade: %d' % (Nome, Idade))
# %s para string
# %d para int
# %f para float
# %.2f para float
# %r para boolean

Nome2, Idade2 = 'Gabriel', 22.8454
print('Nome %s, idade: %.2f' % (Nome2, Idade2))


# Fazendo a interpolação < python 3.6
print('\nFazendo a interpolacao < python 3.6')
print('Nome: {0}, Idade: {1}'.format(Nome, Idade))

# Fazendo a interpolação > python 3.6
print('\nFazendo a interpolacao > python 3.6')
print(f'Nome: {Nome}, Idade: {Idade}')

# Fazendo interpolacao com template
print('\nusando template')
s = Template('Nome: $nome e Idade: $idade')
print(s.substitute(nome=Nome, idade=Idade))
