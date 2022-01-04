def soma(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == "__main__":
    print(soma(2, 2))
    print(soma_3(1, 2, 3))
    # Packing
    print(soma_n(1, 1, 1, 1, 1, 1, 1, 1, 1))

    # Unpacking
    nums = (3, 2, 3)
    print(soma_3(*nums))
