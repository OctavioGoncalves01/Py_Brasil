import time

TemperaturaMeses = []
Cont = []

def Cab():
    print('---------------------------------')
    time.sleep(0.25)

for C in range(1,13):
    Cab()
    TemperaturaMeses.append(float(input(f'Digite a temperatura media do {C}° Mês:')))

MediaAnual = sum(TemperaturaMeses) / len(TemperaturaMeses)

for Temp in TemperaturaMeses:
    if Temp > MediaAnual:
        T = TemperaturaMeses.index(Temp)
        Cont.append(T)

Cab()
print('')
print(f'Média anual: {MediaAnual:2.2f}°C')
print('')

for M in Cont:
    Cab()
    if M == 0:
        print('O mes de Janeiro teve a temperatura maior que a média de ', TemperaturaMeses[M],'°C.')
    if M == 1:
        print('O mes de Fevereiro teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 2:
        print('O mes de Março teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 3:
        print('O mes de Abril teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 4:
        print('O mes de Maio teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 5:
        print('O mes de Junho teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 6:
        print('O mes de Julho teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 7:
        print('O mes de Agosto teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 8:
        print('O mes de Setembro teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 9:
        print('O mes de Outubro teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 10:
        print('O mes de Novembro teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')
    if M == 11:
        print('O mes de Dezembro teve a temperatura maior que a média.', TemperaturaMeses[M],'°C.')


#\\\\\\\\\\\\\\