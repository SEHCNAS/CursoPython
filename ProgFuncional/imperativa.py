from locale import setlocale, LC_ALL
from calendar import month_name, mdays

# portugues
setlocale(LC_ALL, 'pt_BR')

print('Meses com 31 dias')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(month_name[mes])