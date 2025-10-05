num = int(input("Enter number: "))
temp = num
summ = 0

while temp > 0:
    rem = temp % 10
    summ += rem
    temp//=10

if num % summ == 0:
    print(f'{num} is Harshad number')
else:
    print(f'{num} is not Harshad number')