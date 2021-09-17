def Temperatura(F):
    C = 5 * ((F-32) / 9)
    return C

Fahrenheit=float(input('Digite a temperatura em Fahrenheit: '))

print(f'A temperatura em Celcius é {Temperatura(Fahrenheit):2.3f}°.')


#\\\\\\\\\\\\\\