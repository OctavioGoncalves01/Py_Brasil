Numero = str(input('Digite seu telefone: '))
NF =[]
if (len(Numero.replace('-', '')) <= 7):
    Numero = '3'+Numero


NNumero = '3' + Numero
ForN = (Numero.replace('-', ''))

for N in ForN:
    NF.append(N)
    if len(NF) == 4:
        NF.append('-')
 

print(f'Número sem formatação:', Numero.replace('-', ''))
print(f'Número com formatação:', Numero)
print(f'Número Corrigido', str(NF).replace(',', '').replace("[]", ''))