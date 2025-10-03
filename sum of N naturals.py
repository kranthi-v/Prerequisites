#By using for loop

N = int(input("Enter a Number: "))
summ = 0
for i in range(1, N+1):
    summ+=i
print(summ)

#By using functions

def summ(num):
    if num ==1:
        return 1
    return num + summ(num-1)

num = int(input("Enter a Number: "))
print(summ(num))