def Reverter(N):
    L = []
    
    for C in range(0, len(N)):
        L.append(N[C:C+1])

    Inverso = list(reversed(L))
    return str(Inverso).strip('[]').strip(" '' ").strip(',')

Num = (input('Digite:  '))

print(Reverter(Num))
