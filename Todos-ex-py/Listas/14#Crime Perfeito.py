Perguntas = []
P = 0

P1 = str(input("Telefonou para a vítima?  [S/N]:\n")).upper()
P2 = str(input("Esteve no local do crime?  [S/N]:\n")).upper()
P3 = str(input("Mora perto da vítima?  [S/N]:\n")).upper()
P4 = str(input("Devia para a vítima?  [S/N]:\n")).upper()
P5 = str(input("Já trabalhou com a vítima?  [S/N]:\n")).upper()

Perguntas.append(P1)
Perguntas.append(P2)
Perguntas.append(P3)
Perguntas.append(P4)
Perguntas.append(P5)

if Perguntas[1] == 'S':
    print('Suspeito')
if (Perguntas[2] == 'S') or (Perguntas[3] == 'S'):
    print('Cúmplice')
if Perguntas[4] == 'S':
    print('Assassino')
else:
    print('Inocente')

print(Perguntas)


#\\\\\\\\\\\\\\