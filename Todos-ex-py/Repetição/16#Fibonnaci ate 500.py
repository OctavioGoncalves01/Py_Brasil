PrimeiroTermo = 1
SegundoTermo = 1
TerceiroTermo = PrimeiroTermo+ SegundoTermo


while (PrimeiroTermo < 500) and (PrimeiroTermo > 499):
    print(PrimeiroTermo)
    PrimeiroTermo = SegundoTermo
    SegundoTermo = TerceiroTermo
    TerceiroTermo = PrimeiroTermo+SegundoTermo


#\\\\\\\\\\\\\\