def ExPeso(P):
    if P < 50:
        print('Carga aceita, sem multa.')
    elif P>=50:
        Multa=(P-50)*4
        print(f'Atenção!! Peso excedido {P-50}kg \nA multa seré de R${Multa:3.2f}.')

Peso=float(input('Digite o peso dos peixes: '))
ExPeso(Peso)


#\\\\\\\\\\\\\\
