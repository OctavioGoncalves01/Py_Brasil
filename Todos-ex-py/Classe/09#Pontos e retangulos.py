class Ponto:
    def __init__(self, PontoX, PontoY):
        self.PontoX = PontoX
        self.PontoY = PontoY
    def Retorno(self):
        return 'Ponto: %s, %s' % repr(self.PontoX), repr(self.PontoY)

class Retangulo:
    def __init__(self, Largura, Altura):
        self.Largura = Largura
        self.Altura = Altura
    def centro(self):
        X_centro = (self.Largura.PontoX + self.Altura.PontoX) / 2.0
        Y_centro = (self.Largura.PontoY + self.Altura.PontoY) / 2.0
        return Ponto(X_centro, Y_centro)

CantoX1 = input("Entre a coordenada x do canto inferior esquerdo: ")
CantoY1 = input("Entre a coordenada y do canto inferior esquerdo: ")
Canto1 = (CantoX1, CantoY1)

CantoX2 = input("Entre a coordenada x do canto superio direito: ")
CantoY2 = input("Entre a coordenada y do canto superio direito:")
Canto2 = (CantoX2, CantoY2)

Objeto = Retangulo(Canto1, Canto2)

print(f'{Objeto.centro()}')

