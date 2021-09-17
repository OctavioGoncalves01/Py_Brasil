QntProdutos = int(input('Quantidade de produtos: '))


print('Lojas Quase Dois - Tabela de preços:')
for C in range(1, 51):
    ValorPagar = QntProdutos*1.99

    if ValorPagar == C*1.99:
        print(f'[Produto(s) {C}  :   R${C*1.99}]')
        break
    else:
        print(f'Produto(s) {C}  :   R${C*1.99}')


#\\\\\\\\\\\\\\