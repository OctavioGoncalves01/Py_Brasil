def Media(x,y):
    M = x/y
    return M

NumeroCds = 1
PrecoTotal = 0

while True:
    Preco = float(input(f'Digite o preço do {NumeroCds}° Cd: R$'))
    NumeroCds+=1
    PrecoTotal+=Preco
    Pergunta = str(input('Deseja continuar [S/N]:  ')).upper()
    if Pergunta == 'N':
        break

MediaPreco = Media(PrecoTotal, NumeroCds)

print(f'A média de preço dos Cds é : R${MediaPreco:2.2f}')


#\\\\\\\\\\\\\\