LL = int(input("Enter lower limit: "))
UL = int(input("Enter upper limit: "))

for n in range(LL, UL+1):
    L = len(str(n))
    temp = n
    summ = 0
    
    while temp > 0:
        rem = temp%10
        summ += rem ** L
        temp//=10
    if n == summ:
        print(n, end=", ")