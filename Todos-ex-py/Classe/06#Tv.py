class Tevelisao:
    def __init__(self, Chanal, Som, Estado):
        self.Chanal = Chanal
        self.Som = Som
        self.Estado = Estado

    def Ligar(self):
        print('Ligando Tv')
        self.Estado = 'on'

    def MudarCanal(self):
        Canal = float(input('Digite o número do canal: '))
        while Canal >= 100:
            Canal = 99
        else:
            self.Chanal = Canal
            print(f'Mudando para Chanal {Canal}')
                    
        
    def Volume(self):
        Volu = int(input('Digite o volume para o aparelho: '))
        while Volu < 101:
            Volu = 100
        if Volu > 75:
            print('!!Ouvir sons alto por muito tempo pode danificar sua audição!!')
        self.Som = Volu

    def Desligar(self):
        print('Desligando Tv')
        self.Estado = 'off'

Tv = Tevelisao(1,10, 'off')

Tv.Ligar()
print(Tv.Estado, Tv.Chanal, Tv.Som)
print('')
Tv.MudarCanal()
Tv.Volume()
print('')
Tv.Desligar()
print(Tv.Estado, Tv.Chanal, Tv.Som)
