Fib=[]
Pt=1
St=1
Tt=Pt+St
for X in range(1,16):
    Fib.append(Pt)
    Pt=St
    St=Tt
    Tt=St+Pt

for X in Fib:
    print(f'**[{X}]**')


#\\\\\\\\\\\\\\