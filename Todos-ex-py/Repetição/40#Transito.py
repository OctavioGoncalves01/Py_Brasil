import time

CodCidade = []
TotalVeiculos = []
TotalAcidentes = []
Soma = 0
ContCity = 0

def Cab():
    print('----------------------')
    time.sleep(0.35)

def MaiorAcidentes (A):
    Aci = max(A)
    Cod = A.index(Aci)
    return Cod

def MenorAcidentes (A):
    Aci = min(A)
    Cod = A.index(Aci)
    return Cod

def MediaCarros(X):
    Media = sum(X)/len(X)
    return Media


print('Pesquisa de trânsito: ')
for N in range(1,6):
    Cab()
    CodCidade.append(str(input('Digite o código da cidade: ')))
    TotalVeiculos.append(int(input('Digite o total de veiculos: ')))
    TotalAcidentes.append(int(input('Digite o total de acidentes com vítimas: ')))

AcidentesAltos = MaiorAcidentes(TotalAcidentes)
AcidentesBaixos = MenorAcidentes(TotalAcidentes)
MediaVeiculos = MediaCarros(TotalVeiculos)

Cab()
print('Resultado:')
print('')
print(f'A cidade com mais acidentes é {CodCidade[AcidentesAltos]} com {TotalAcidentes[AcidentesAltos]}')
print('')
print(f'A Cidade com menos acidentes é {CodCidade[AcidentesBaixos]} com {TotalAcidentes[AcidentesBaixos]}')
print('')
print(f'A media de veiculos é {MediaVeiculos:2.1f}')

print('')
for c in TotalAcidentes:
    if c < 2000:
        Soma+=c
        ContCity+=1 

print('A media de Acidentes em cidades com menos de 2000 carros é:', Soma/ContCity)


#\\\\\\\\\\\\\\