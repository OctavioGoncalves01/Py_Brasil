
def Palindromo(F):
    ContarioF = F[::-1]

    if F == ContarioF:
        print('Esta frase é um Palíndromo')
    else:
        print('A frase não é um Palíndromo')

Frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
Palindromo(Frase)


#\\\\\\\\\\\\\\