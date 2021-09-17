numbers = []

for C in range(1,11):
    numbers.append(float(input('Digite: ')))

newList = [num for num in reversed(numbers)]
print(newList)


#https://www.delftstack.com/pt/howto/python/python-reverse-a-list/
#\\\\\\\\\\\\\\