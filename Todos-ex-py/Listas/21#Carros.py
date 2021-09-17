import time

def Cab():
    print('-----------------------')
    time.sleep(0.25)

Modelos = ['Gol', 'Fiesta', 'Uno', 'Opala', 'Fusca']
Consumo = [13.3, 11.6, 10.1, 9.5, 9.7]

Cab()
print('Resultado da pesquisa:')
for C in range(0, len(Consumo)):
    Cab()
    print(f'Modelo: {Modelos[C]}           Consumo: {Consumo[C]}\nValor gasto com 1000 Km rodados: R${(1000 / Consumo[C]) * 2.25:2.2f}')

Cab()
print(f'Carro mais economico: {Modelos[Consumo.index(max(Consumo))]}')


#\\\\\\\\\\\\\\