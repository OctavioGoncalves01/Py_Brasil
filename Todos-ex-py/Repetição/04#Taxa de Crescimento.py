PaisA=80000
PaisB=200000
Cont=0

while PaisA < PaisB:
    PaisA+=(PaisA*3/100)
    PaisB+=(PaisB*1.5/100) 
    Cont+=1

print(f'Vai demorar {Cont} ano(s) para o Pais A passar o Pais B')
print(f'População de Pais A: {PaisA:2.2f}Hab.\nPopulação de Pais B: {PaisB:2.2f}Hab.')


#\\\\\\\\\\\\\\