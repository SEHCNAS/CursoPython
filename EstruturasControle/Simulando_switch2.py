def get_DiaSemana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'
    }
    return dias.get(dia, '***Dia invalido***')


if __name__ == '__main__':
    for dia in range(0, 9):
        if dia in range(2, 7):
            print(f'{dia} = {get_DiaSemana(dia)} - dia de semana!')
        elif dia == 1 or dia == 7:
            print(f'{dia} = {get_DiaSemana(dia)} - final de semana!')
        else:
            print(f'{dia} = {get_DiaSemana(dia)}')
