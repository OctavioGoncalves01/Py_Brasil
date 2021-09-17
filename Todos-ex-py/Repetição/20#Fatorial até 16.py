Soma = 1

while True: 
    Fatorial = int(input('Digite um número:\n [Ele deve ser inteiros positivos e menores que 16.]\n'))

    if (Fatorial > 0 ) and (Fatorial <16):
        for f in range(Fatorial, 1, -1):
            Soma = Soma*f

        print(f'A soma é {Soma}')
        Pergunta = str(input('Deseja continuar: [S/N]\n')).upper()

        if Pergunta != 'S':
            break

print('Obrigado por usar!!')


#\\\\\\\\\\\\\\