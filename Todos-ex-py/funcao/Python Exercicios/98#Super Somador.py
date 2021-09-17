def SuperSomador(x,y):
    SS=0
    for N in range(x,y+1):
        SS=SS+N
    return SS

Inicio=int(input('Digite o primeiro número: '))
Fim=int(input('Digite o ultimo número: '))

print(SuperSomador(Inicio, Fim))


#\\\\\\\\\\\\\\