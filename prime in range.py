LL = int(input("Enter lower limit: "))
UL = int(input("Enter upper limit: "))

for i in range(LL, UL + 1):
    if i > 1:
        for j in range(2, i//2 + 1):
            if i % j == 0:
                break
        else:
            print(i)