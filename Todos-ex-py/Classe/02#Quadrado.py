class Box:
    def __init__(self, Altura, Largura):
        self.Altura = Altura
        self.Largura = Largura

    def MudarLados(self, Altura, Largura):
        Perg = str(input('Deseja mudar os lados [S/N]: ')).upper()
        if Perg == 'S':
            self.Altura = int(input('Qual a nova Altura: '))
            self.Largura = int(input('Qual a nova largura: '))

    def Area(self):
        print(f'A área deste quadrado é: {self.Largura} x {self.Altura} = {self.Altura * self.Largura}')

Quadrado1 = Box(15, 10)

print(f'Altura = {Quadrado1.Altura}, Largura = {Quadrado1.Largura}')
Quadrado1.MudarLados(Quadrado1.Altura, Quadrado1.Largura)
Quadrado1.Area()


#\\\\\\\\\\\\\\