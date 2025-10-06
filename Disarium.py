n = int(input('Enter a number: '))
temp = n
summ = 0
l = len(str(n))

while temp > 0:
    rem = temp % 10
    summ += rem ** l
    l = l-1
    temp//=10
if summ == n:
    print(f'{n} is disarium number')
else:
    print(f'{n} is not disarium number')
