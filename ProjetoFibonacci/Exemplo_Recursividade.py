def Imprimir(NumeroMaximo, NumeroAtual):
    # Função que chama a si mesma
    if NumeroAtual >= NumeroMaximo:
        return
    print(NumeroAtual)
    Imprimir(NumeroMaximo, NumeroAtual + 1)


Imprimir(10, 1)
