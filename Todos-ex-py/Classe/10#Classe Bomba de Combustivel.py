class Bomba_Combustives:
    def __init__(self, Tipo_Combustivel, Valor_Combustivel, Quantidade_Combustivel):
        self.Tipo_Combustivel = Tipo_Combustivel
        self.Valor_Combustivel = Valor_Combustivel
        self.Quantidade_Combustivel = Quantidade_Combustivel
        self.Bomba = 528

    def Abasteca_Por_Favor(self):
        Quantia = float(input('Informe o valor a ser abastecido: '))
        
