def fatorial(n):
    return n * (fatorial(n-1) if (n -1) > 1 else 1)

if __name__ == '__main__':
    resultado = fatorial(10)
    print(resultado)