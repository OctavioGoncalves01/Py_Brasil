Idade = []
Altura = []

def Cab():
    print('---*---*---*---')

for C in range(1,6):
    Cab()
    Idade.append(int(input('Digite sua idade: ')))
    Altura.append(float(input('Digite sua altura: ')))

Cab()
print(Idade, Altura)

Cab()
InverteAltura = [altura for altura in reversed(Altura)]
InvertIdade = [idade for idade in reversed(Idade)]
print(InverteAltura, InvertIdade)


#\\\\\\\\\\\\\\