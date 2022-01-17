def todos_parm(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_parm('a', 'b', 'c')
    todos_parm('a', 'b', 'c', legal=True, valor=1)
