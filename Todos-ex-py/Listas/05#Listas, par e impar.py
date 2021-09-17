ListaComum = []
Par = []
Impar = []

for L in range(1,21):
    N = int(input('Digite um número: '))
    ListaComum.append(N)

for P in ListaComum:
    if P % 2 == 0:
        Par.append(P)
    elif P % 2 != 0:
        Impar.append(P)

print('Numeros: ', ListaComum)
print('Par:     ', Par)
print('Impar:   ', Impar)


#\\\\\\\\\\\\\\