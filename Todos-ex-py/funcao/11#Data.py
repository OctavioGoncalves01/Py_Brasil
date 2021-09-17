def Extanso(X):
    print('Data por extenço: ')

    if X[3:5] == '01':
        print(f'{X[0:2]} de Janeiro de {X[6:10]}.')
    elif X[3:5] == '02':
        print(f'{X[0:2]} de Fevereiro de {X[6:10]}.')
    elif X[3:5] == '03':
        print(f'{X[0:2]} de Março de {X[6:10]}.')
    elif X[3:5] == '04':
        print(f'{X[0:2]} de Abril de {X[6:10]}.')
    elif X[3:5] == '05':
        print(f'{X[0:2]} de Maio de {X[6:10]}.')
    elif X[3:5] == '06':
        print(f'{X[0:2]} de Junho de {X[6:10]}.')
    elif X[3:5] == '07':
        print(f'{X[0:2]} de Julho de {X[6:10]}.')
    elif X[3:5] == '08':
        print(f'{X[0:2]} de Agosto de {X[6:10]}.')
    elif X[3:5] == '09':
        print(f'{X[0:2]} de Setembro de {X[6:10]}.')
    elif X[3:5] == '10':
        print(f'{X[0:2]} de Outubro de {X[6:10]}.')
    elif X[3:5] == '11':
        print(f'{X[0:2]} de Novembro de {X[6:10]}.')
    elif X[3:5] == '12':
        print(f'{X[0:2]} de Dezembro de {X[6:10]}.')
    else:
        print('Nell')

Data = input('Digite a data com este formaato [DD/MM/AAAA]:\n')
Extanso(Data)


#\\\\\\\\\\\\\\