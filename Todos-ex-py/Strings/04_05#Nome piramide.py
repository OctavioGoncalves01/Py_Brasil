Nome = str(input('Informe seu nome: ')).upper()

for S in range(0, len(Nome)):
    print(Nome[0:S+1])

print('')

for N in range(len(Nome) +1, 0, -1):
    print(Nome[0:N-1])


#\\\\\\\\\\\\\\