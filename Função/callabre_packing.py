def cal_preco(preco_final, cal_imposto, *args):
    return preco_final + (preco_final * cal_imposto(*args))


def imposto_x(importante):
    return 0.22 if importante else 0.13


def imposto_y(explosivo, grau_perigo=1):
    return 0.11 * grau_perigo if explosivo else 0


if __name__ == '__main__':

    preco_bruto = 134.98
    preco_final = cal_preco(preco_bruto, imposto_x, True)
    preco_final = cal_preco(preco_final, imposto_y, True, 1.5)
    print(f'preco final : {preco_final}')
