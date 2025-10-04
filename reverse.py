#By slicing
num = int(input("Enter a number:"))
print(str(num)[::-1])

#By loop
num = int(input("Enter a number:"))
rev = 0
while num > 0:
    rem = num%10
    rev = rev*10 + rem
    num//=10
print(rev)