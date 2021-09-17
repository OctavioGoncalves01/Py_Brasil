def inverter(txt):
  return txt[::-1]

N = str(input('Digite um número inteiro e positivo:\n'))

while N.isalnum() == False:
    N = str(input('Digite um número inteiro e positivo:\n')).isalnum()

print(inverter(N))


#\\\\\\\\\\\\\\
#Copiei a funcao: https://www.horadecodar.com.br/2020/12/10/como-inverter-uma-string-em-python/