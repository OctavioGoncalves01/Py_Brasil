Temperatura = []

while True:
    T = input('Digite a temperatura em C° [*F* para Sair]: \n').upper()
    if T == 'F':
        break
    else:
        T = float(T)
        Temperatura.append(T)

print('')
print(f'A maior temperatura registrada foi de {max(Temperatura)}°C.')
print(f'A menor temperatura registrada foi de {min(Temperatura)}°C.')
print(f'A media foi de {sum(Temperatura)/len(Temperatura):2.2f}')
print('')
print(Temperatura)


#\\\\\\\\\\\\\\