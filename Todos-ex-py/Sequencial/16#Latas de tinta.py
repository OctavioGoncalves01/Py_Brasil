def Area(X,Y):
    A=X*Y
    return A

Altura=float(input('Digite a altura da parede: '))
Largura=float(input('Digite a lagura da parede: '))

MetrosQua=Area(Altura, Largura)
Litros=MetrosQua/3
Latas=Litros/18
Valor=80*Latas

print(f'O tamanho da parede será: {MetrosQua:3.2f}\nO Valor em será R${Valor:3.2f}. E utilizara  {Latas:2.1f} lata(s).')