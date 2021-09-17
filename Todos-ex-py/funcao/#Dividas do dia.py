def ValorPagamento(X,Y):
    if Y>=1:
        Valor=(X+1.03)+(X*(Y*0,1))
    return Valor


Pagamento=float(input('Digite o valor: R$'))
Dias=int(input('Digite os dias em atraso: '))

print(ValorPagamento(Pagamento,Dias))


          