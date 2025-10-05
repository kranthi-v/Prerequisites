N = int(input("Enter number: "))
temp = N
summ = 0
L = len(str(N))

while temp > 0:
    rem = temp%10
    summ += rem ** L
    temp//=10
if N == summ:
    print(f'{N} is Armstrong number')
else:
    print(f'{N} is not a Armstrong number')