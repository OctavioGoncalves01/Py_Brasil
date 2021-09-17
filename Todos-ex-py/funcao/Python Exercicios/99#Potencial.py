def Potencial(B, E):
    G=B**E
    return G
    
Base=int(input('Digite a base: '))
Expo=int(input('Digite o exponenciador: '))

print(Potencial(Base, Expo))