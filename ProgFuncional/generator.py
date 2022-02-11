def cores_arcoiris():
    # yield = retorna um valor para cada next da função
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'

if __name__ == '__main__':

    generator = cores_arcoiris()
    print(type(generator))
    while True:
        print(next(generator))