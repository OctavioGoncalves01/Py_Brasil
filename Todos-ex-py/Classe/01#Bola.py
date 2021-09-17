class Bola:
    def __init__(self, Cor, Circunferencia, Material):
        self.Cor = Cor
        self.Circunrerencia = Circunferencia 
        self.Material = Material

    def MostraCor(self):
        print(f'Cor: {self.Cor}')

    def TrocaCOr(self):
        self.Cor = str(input('Digite a nova cor: '))

Ball = Bola('Azul', '20cm', 'Plastico')

Ball.MostraCor()
Ball.TrocaCOr(Ball.Cor)
Ball.MostraCor()


#\\\\\\\\\\\\\\