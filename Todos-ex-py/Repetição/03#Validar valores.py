Nome = str(input('Digite seu nome:'))
while len(Nome) < 3:
    Nome = str(input('Digite seu nome:'))

Sexo = str(input('Sexo F/M: ')).upper()
while (Sexo != 'F') and (Sexo != 'M'): 
    Sexo = str(input('Sexo F/M: ')).upper()

Idade = int(input('Digite a sua idade: '))
while Idade < 0 or Idade > 150:
    Idade = int(input('Digite a sua idade: '))

Salario = float(input('Digite seu salario: R$'))
while Salario <= 0:
    Salario = float(input('Digite seu salario: R$'))

EstadoCivil=str(input('Estado Civil:\nSolteiro = S; Casado = C; Viuvo = V; Divorciado = D: ')).upper()
while EstadoCivil != 'S' and 'C' and 'V' and 'D':
    EstadoCivil=str(input('Estado Civil:\nSolteiro = S; Casado = C; Viuvo = V; Divorciado = D')).upper()

print('Cadastro realizado:')
print(f'Nome: {Nome}      Sexo:{Sexo}     Idade: {Idade}ano(s)')
print(f'Estado Civil: Cod = *{EstadoCivil}*      Salario: R${Salario}')


#\\\\\\\\\\\\\\