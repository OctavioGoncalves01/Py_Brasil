DiciNum = {1:'um', 2:'dois', 3:'tres', 4:'quatro', 5:'cinco', 6:'seis', 7:'sete', 8:'oito', 9:'nove', 10:'dez',
11:'onze', 12:'doze', 13:'treze', 14:'quatorze', 15:'quinze', 16:'dezesseis', 17:'dezessete', 18:'dezoito', 19:'dezenove', 
20:'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa',}

num = int(input('Digite um numero entre um e noventa e nove: '))

decimal = num // 10 * 10
unidade = num % 10

if num <= 20:
    print(DiciNum[num])
else:
    print(f'{DiciNum[decimal]} e {DiciNum[unidade]}')

#https://gist.github.com/willianribeiro/c2260ad1b34699e37f85a07d6c09e67f