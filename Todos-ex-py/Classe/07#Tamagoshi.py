import random
Cont = 0

class Tamagoshi:
    def __init__(self, Nome_Tamagoshi, Idade_Tamagoshi, Fome_Tamagoshi, Saude_Tamagoshi):
        self.Nome_Tamagoshi = Nome_Tamagoshi
        self.Idade_Tamagoshi = Idade_Tamagoshi
        self.Fome_Tamagoshi = Fome_Tamagoshi
        self.Saude_Tamagoshi = Saude_Tamagoshi
        self.Dias = Cont

    def Novo_Nome(self):
        self.Nome_Tamagoshi = str(input('Digite o novo nome para o Tamagoshi:\n'))
        return self.Nome_Tamagoshi

    def Fome(self):
        if self.Fome_Tamagoshi >= 90:
            print('Estou sem fome')
        elif (self.Fome_Tamagoshi >= 60) and (self.Fome_Tamagoshi <90):
            print('Estou com um pouco de fome')
        elif  (self.Fome_Tamagoshi >= 40) and (self.Fome_Tamagoshi <60):
            print('Estou com fome')
        elif (self.Fome_Tamagoshi >= 20) and (self.Fome_Tamagoshi <40):
            print('Estou morrendo de fome')
        else:
            print('Estou varado de fome')
        return self.Fome_Tamagoshi

    def Saude(self):
        if self.Saude_Tamagoshi == 100:
            print('Estou perfeitamente bem')
        elif (self.Saude_Tamagoshi <=99) and (self.Saude_Tamagoshi > 75):
            print('Estou bem')
        elif (self.Saude_Tamagoshi <=75) and (self.Saude_Tamagoshi > 50):
            print('Estou mais ou menos')
        elif (self.Saude_Tamagoshi <=50) and (self.Saude_Tamagoshi > 25):
            print('Estou doente')
        elif (self.Saude_Tamagoshi <=25) and (self.Saude_Tamagoshi > 5):
            print('Estou muito doente')
        else:
            print('Estou morrendo')
        return self.Saude_Tamagoshi

    def Tempo(self):
        self.Dias = self.Dias + 1
        self.Fome_Tamagoshi -= 25
        self.Saude_Tamagoshi -= 10
        if self.Saude_Tamagoshi and self.Fome_Tamagoshi <= 0:
            print(f'{self.Nome_Tamagoshi} esta morto')
            

Fome = random.randint(0,100)
Saude = random.randint(0, 100)

Animal01 = Tamagoshi('Felisberto', 0, Fome, Saude)

print(Animal01.Nome_Tamagoshi, Animal01.Fome_Tamagoshi, Animal01.Saude_Tamagoshi)
Animal01.Tempo()
print(Animal01.Nome_Tamagoshi, Animal01.Fome_Tamagoshi, Animal01.Saude_Tamagoshi)
Animal01.Novo_Nome()
Animal01.Tempo
print(Animal01.Nome_Tamagoshi, Animal01.Fome_Tamagoshi, Animal01.Saude_Tamagoshi)