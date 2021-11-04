# Criar Dicionario
DicionarioPessoa = {'Nome': 'Gabriel', 'Idade': 22, 'Cursos': ['c#', 'Python']}
print(type(DicionarioPessoa))
print(len(DicionarioPessoa))
print(DicionarioPessoa)

# Acessar dados do dicionario
print(DicionarioPessoa['Nome'])
print(DicionarioPessoa['Idade'])
print(DicionarioPessoa['Cursos'])
print(DicionarioPessoa['Cursos'][0])
print(DicionarioPessoa['Cursos'][1])

# Pegar as chaves do dicionario
print(DicionarioPessoa.keys())

# Pegar os valores do dicionario
print(DicionarioPessoa.values())
print(DicionarioPessoa.get('Idade'))
print(DicionarioPessoa.get('Item_nao_existente', ['Volta valor padrao']))

# pegar chaves + valores
print(DicionarioPessoa.items())

# Adionanco e modificando os valores do dicionario
DicionarioPessoa['Idade'] = 23
DicionarioPessoa['Cursos'].append('Genexus')
print(DicionarioPessoa)

# le e exclui o valor
print(DicionarioPessoa.pop('Idade'))
print(DicionarioPessoa)

# Excluir valores
del DicionarioPessoa['Cursos']
print(DicionarioPessoa)

# Limpa todo o dicionario
DicionarioPessoa.clear()
print(DicionarioPessoa)

# Adicionar itens no dicionario
DicionarioPessoa.update({'Idade': 22, 'Sexo': 'M'})
print(DicionarioPessoa)
