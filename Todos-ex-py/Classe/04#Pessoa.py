class Pessoa:
    def __init__(self, Nome, Idade, Altura, Peso):
        self.Nome = Nome
        self.Idade = Idade
        self.Altura = Altura
        self.Peso = Peso

    def Engordar(self):
        NPeso = float(input('Quantos Kg Ganhou: '))
        self.Peso += NPeso

    def Emagracer(self):
        NPeso = float(input('Quantos Kg Perdeu: '))
        self.Peso -= NPeso

    def Envelhecer(self):
        if self.Idade <= 21:
            self.Altura += 0.005
            self.Peso += 0.5
            self.Idade += 1
        return self.Nome, self.Idade 

Humano1 = Pessoa('Octavio', 19, 1.75, 55.5)
Humano2 = Pessoa('Mirai', 16, 1.62, 50.1 )

print(f'A pessoa {Humano1.Nome} tem {Humano1.Idade} anos de idade, Peso {Humano1.Peso}, Altura {Humano1.Altura:2.2f}')
print(f'A pessoa {Humano2.Nome} tem {Humano2.Idade} anos de idade, Peso {Humano2.Peso}, Altura {Humano2.Altura:2.2f}')

Humano1.Envelhecer()
Humano2.Envelhecer()

print(f'A pessoa {Humano1.Nome} tem {Humano1.Idade} anos de idade, Peso {Humano1.Peso}, Altura {Humano1.Altura}')
print(f'A pessoa {Humano2.Nome} tem {Humano2.Idade} anos de idade, Peso {Humano2.Peso}, Altura {Humano2.Altura}')

Humano2.Emagracer()
Humano1.Engordar()

Humano1.Envelhecer()
Humano2.Envelhecer()

print(f'A pessoa {Humano1.Nome} tem {Humano1.Idade} anos de idade, Peso {Humano1.Peso}, Altura {Humano1.Altura}')
print(f'A pessoa {Humano2.Nome} tem {Humano2.Idade} anos de idade, Peso {Humano2.Peso}, Altura {Humano2.Altura}')


#\\\\\\\\\\\\\\