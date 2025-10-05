num = int(input("enter number: "))
summ = 0

for i in range(1, num//2+1):
    if num % i == 0:
        summ += i

if num == summ:
    print(f'{num} is perfect number')
else:
    print(f'{num} is not perfect number')