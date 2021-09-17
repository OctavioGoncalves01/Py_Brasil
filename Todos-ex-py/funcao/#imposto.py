def SomaImposto(TaxaImposto, Custo):
    Valor=Custo+(Custo*TaxaImposto/100)
    return Valor

Preco=float(input('Digite o valor do produto: R$'))
Taxa=float(input('Digite o valor da taxa: '))

print(f'O valor do produto com o imposto é: R${SomaImposto(Taxa, Preco):4.2f}')


#\\\\\\\\\\\\\\