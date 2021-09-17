def Area(X,Y):
    A=X*Y
    return A

Altura=float(input('Digite a altura da parede: '))
Largura=float(input('Digite a lagura da parede: '))

MetrosQua=Area(Altura, Largura)
Litros=MetrosQua/6

PrecoLata=80
PrecoGalao=25
Lata=18
Galao=3.6

print(Litros)
print(f'{(Litros/Lata)*PrecoLata:3.2f}')
print(f'{(Litros/Galao)*PrecoGalao:3.2f}')