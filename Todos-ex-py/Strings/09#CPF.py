CPF = str(input('Informe seu CPF [xxx.xxx.xxx-xx]:\n'))
if (CPF[3:4] and CPF[7:8] == '.') and (CPF[11:12] == '-'):
    print('CPf Valido')
else:
    print('CPf Invalido')


#\\\\\\\\\\\\\\