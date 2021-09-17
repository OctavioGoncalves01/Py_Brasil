PrimeiroTermo = 1
SegundoTermo = 1
TerceiroTermo = PrimeiroTermo+ SegundoTermo

N = int(input('Até qual termo deseja ver na sequencia de Fibonnaci: '))

for F in range(1, N+1):
    print(PrimeiroTermo)
    PrimeiroTermo = SegundoTermo
    SegundoTermo = TerceiroTermo
    TerceiroTermo = PrimeiroTermo+SegundoTermo


#\\\\\\\\\\\\\\