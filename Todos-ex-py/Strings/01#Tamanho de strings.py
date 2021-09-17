def Comparar(X, Y):
    print('Compara duas Strings:')
    print(f'Tamanho da primeira frase: {len(X)} Caracteres.\nFrase 01:[{X}]')
    print('')
    print(f'Tamanho da segunda frase: {len(Y)} Caracteres.\nFrase 02: [{Y}]')
    print('')

    if len(X) == len(Y):
        print('Ambas as Strings possuem o mesmo tamanho.')
    else:
        print('As Strings possuem tamanhos diferente.')
    print('')
    if (X == Y) == True:
        print('As strings possuem o mesmo conteúdo')
    else:
        print('As strings possuem conteúdo diferente')
    
Frase01 = str(input('Digite a primeira frase:\n'))
Frase02 = str(input('Digite a segunda frase:\n'))
print('-----------------------------------')

Comparar(Frase01, Frase02)


#\\\\\\\\\\\\\\