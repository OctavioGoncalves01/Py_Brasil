def Perso(X, Y, Z):
    if Z == 1:
        Z='+-------=======------+'
    elif Z == 2:
        Z='~~~~~~~~:::::::~~~~~~~'
    elif Z == 3:
        Z='<<<<<<<<------->>>>>>>'
    else:
        Z='Digite a opcao valida para bordas!!'
    
    print(Z)
    for C in range(0,Y):
        print(X)
    print(Z)

Pergunta=(input('Digite a mensagem: '))
Vezes=int(input('A mensagem deve aparecer quantas vezes: '))
Borda=int(input('Qual borda deseja usar:\n1[+-------=======------+]\n2[~~~~~~~~:::::::~~~~~~~]\n3[<<<<<<<<------->>>>>>>]\n'))
Perso(Pergunta, Vezes, Borda)


#\\\\\\\\\\\\\\