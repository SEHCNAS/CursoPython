def resultado(primeiro, segundo, terceiro):
    print(f'1) -> {primeiro}')
    print(f'2) -> {segundo}')
    print(f'3) -> {terceiro}')


if __name__ == '__main__':
    podium = {'primeiro': 'Hamiltom',
              'segundo': 'Verstappen',
              'terceiro': 'Vettel'}
    print(resultado(**podium))
