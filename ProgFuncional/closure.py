def multiplica(x):
    def calcular(y):
        return x * y
    return calcular

if __name__ == '__main__':
    # passou a variavel y
    dobro = multiplica(2)
    triplo = multiplica(3)
    print(dobro)
    print(triplo)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')