def log(function):
    def decorator(*args, **kwargs):
        print(f'inicio da chamada da funcao: {function.__name__}')
        print(f'paramentros nao nomeados: {args}')
        print(f'paramentros nomeados: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'o resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def subtracao(x, y):
    return x - y


if __name__ == '__main__':
    print(f'Resultado na main:{soma(5, 10)}\n')
    print(f'Resultado na main:{subtracao(5, y=10)}')
