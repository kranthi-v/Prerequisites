num = int(input("Enter a number:"))
summ = 0

while num>0:
    rem = num%10
    summ += rem
    num//=10
    
print(summ)