AbonoSalarios = []

def CalculoAbono(X):
    NovaLista = []
    for C in X:
        S = C * 20 / 100
        if S <= 100:
            NovaLista.append(100)
        else:
            NovaLista.append(S)

    return NovaLista

while True:
    Salario = float(input('Digite o Valor do Salario: R$'))
    if Salario == 0:
        break
    else:
        AbonoSalarios.append(Salario)

Con100 = 0
Cont = len(AbonoSalarios)
Lista = (CalculoAbono(AbonoSalarios))
print('')

print('Salario:                     Abono:')
for C in AbonoSalarios:
    print(f'R$ {C:2.2f}:                    R${Lista[AbonoSalarios.index(C)]:0.2f}')
print('')
print('Valor gasto com os abonos:                    R$', sum(Lista))
for X in Lista:
    if X <= 100:
        Con100 += 1
print('')
print('O total de colaboradors que receberam o piso foi de: ', Con100)
print('')
print('O maior valor pago com o abono foi de: R$', max(Lista))


#\\\\\\\\\\\\\\