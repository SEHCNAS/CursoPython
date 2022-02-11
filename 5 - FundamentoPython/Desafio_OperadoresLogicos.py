# Desafio Operadores Logicos

# Os trabalhos

TrabalhoTerca = False
TrabalhoQuinta = False

if TrabalhoTerca and TrabalhoQuinta:
    print('TC 50 + SORVETE')
elif TrabalhoTerca or TrabalhoQuinta:
    print('TC 32 + SORVETE')
else:
    print('FICA EM CASA')

EstaChuvendo = True
print('hoje estou com as roupas ' + ('secas.', 'Molhadas.')[EstaChuvendo])
print('hoje estou com as roupas ' +
      ('secas.' if not EstaChuvendo else 'Molhadas.'))

"""
listaA = [1, 2, 3]
listaB = listaA

listaB[1] = 3

print(listaA[1])
"""
