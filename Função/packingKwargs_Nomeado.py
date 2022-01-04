def resultado(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado(primeiro='Hamiltom',
              segundo='Verstappen',
              terceiro='Vettel')
