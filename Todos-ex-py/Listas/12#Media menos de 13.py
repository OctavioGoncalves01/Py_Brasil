Idade = []
Altura = []
Cont = []

for C in range(1, 31):
    Idade.append(int(input('Digite sua idade: ')))
    Altura.append(float(input('Digite sua altura: ')))

MediaAltura = sum(Altura) / len(Altura)

for High in Altura:
    if High <= MediaAltura:
        A = (Altura.index(High))
        if Idade[A] > 13:
            Cont.append(A)
    
print(f'Existem {len(Cont)} com a altura menor que a media.')


#\\\\\\\\\\\\\\