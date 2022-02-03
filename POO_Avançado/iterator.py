class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __iter__(self):
        return self
    # interator
    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()

if __name__ == '__main__':
    cores = RGB()

    print(next(cores))
    print(next(cores))
    print(next(cores))
    try:
        print(next(cores))
    except StopIteration:
        print('Acabou')

    # Precisa da def __iter__ e __next__ para funcionar
    for cor in RGB():
        print(cor)