Notas = []

for N in range(1,5):
    Notas.append(float(input(f'Digite a {N}° nota do aluno: ')))

Media = sum(Notas)/len(Notas)

print(f'A média do aluno é : {Media:2.2f}')


#\\\\\\\\\\\\\\