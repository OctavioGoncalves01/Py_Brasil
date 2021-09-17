Meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

Data = str(input('Digite a data de seu nascimento [dd/mm/aaaa]:\n'))

if Data[3:5] == '01':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[0]} de {Data[6:10]}')
elif Data[3:5] == '02':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[1]} de {Data[6:10]}')
elif Data[3:5] == '03':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[2]} de {Data[6:10]}')
elif Data[3:5] == '04':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[3]} de {Data[6:10]}')
elif Data[3:5] == '05':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[4]} de {Data[6:10]}')
elif Data[3:5] == '06':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[5]} de {Data[6:10]}')
elif Data[3:5] == '07':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[6]} de {Data[6:10]}')
elif Data[3:5] == '08':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[7]} de {Data[6:10]}')
elif Data[3:5] == '09':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[8]} de {Data[6:10]}')
elif Data[3:5] == '10':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[9]} de {Data[6:10]}')
elif Data[3:5] == '11':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[10]} de {Data[6:10]}')
elif Data[3:5] == '12':
    print(f'Voce nasceu em {Data[0:2]} de {Meses[11]} de {Data[6:10]}')
else:
    print('Data invalida')

