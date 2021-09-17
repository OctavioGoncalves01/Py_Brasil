import random

Alimento = ['Banana']

class Macaco:
    def __init__(self, Nome, Comida):
        self.Nome = Nome
        self.Comida = Comida
        self.Bucho = []

    def Barriga(self):
        print(self.Bucho)
    
    def Alimentar(self, Lanche):
        print('Nhoc!!Nhoc')
        Lanche = self.Comida
        Buxo = self.Bucho
        Buxo.append(Lanche)
    
    def Digestao(self):
        print('Fazendo a digestão')
        Fezes = self.Bucho
        print('Eliminado fezes: ', Fezes)
        self.Bucho = []

Lanche1 = random.choice(Alimento)
Lanche2 = random.choice(Alimento)
Animal01 = Macaco('Chico', Lanche1)
Animal02 = Macaco('Zé', Lanche2)

Animal01.Barriga()
Animal02.Barriga()

Animal01.Alimentar(Lanche1)


Animal01.Barriga()
Animal02.Barriga()

Animal01.Digestao()
Animal02.Digestao()

Animal01.Barriga()
Animal02.Barriga()