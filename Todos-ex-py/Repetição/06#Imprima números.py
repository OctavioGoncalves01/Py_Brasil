Orintacao=str(input('Vertical = V\nLado a lado = L:\n')).upper()

if Orintacao == 'L':
    for c in range(1,21):
        print(c, end=' ')
elif Orintacao == 'V':
    for c in range(1,21):
        print(c)
else:
    print('Digite um valor Correto!')


#\\\\\\\\\\\\\\