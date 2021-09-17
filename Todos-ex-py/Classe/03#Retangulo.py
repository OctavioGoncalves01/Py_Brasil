class Retangulo:
    def __init__(self, Base, Altura):
        self.Base = Base
        self.Altura = Altura
        self.Terreno_Area = Base * Altura
        self.Terreno_Perimetro = (Base * Altura) * 2

    def MudarLados(self):
        Mudar = str(input('Deseja mudar um dos lados [S/N]')).upper()
        if Mudar == 'S':
            self.Base = float(input('Digite o novo tamanho da base [Em metro]: '))
            self.Altura = float(input('Dgite o novo tamanho da Altura [Em metros]: '))

    def Retornar_Valores(self):
        print(f'Base: {self.Base}')
        print(f'Altura: {self.Altura}')

    def Area(self):
        print(f'A área deste terreno é: {self.Altura * self.Base}M.')

    def Perimetro(self):
        print(f'O perimetro deste terreno é de: {(self.Altura * self.Base) * 2}')

    def Piso(self):
        print(f'O tamanho do piso do terreno é de {self.Terreno_Area}m² e o radapé {self.Terreno_Perimetro}m ')

Largura_Terreno = float(input('Digite a largura do terreno: '))
Comprimento_Terreno = float(input('Digite o comprimento do terreno: '))

Terreno = Retangulo(Comprimento_Terreno, Largura_Terreno)

Terreno.Retornar_Valores()
Terreno.Area()
Terreno.Perimetro()
Terreno.Piso()