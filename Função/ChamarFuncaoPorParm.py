def executar(funcao):
    if callable(funcao):
        funcao()
    else:
        print('Função não pode ser chamada')


def bom_dia():
    print("Bom dia")


def boa_tarde():
    print("Boa tarde")


if __name__ == "__main__":
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)
