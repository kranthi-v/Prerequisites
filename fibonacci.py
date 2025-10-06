n = int(input("Enter the no of terms: "))
a,b = 0,1
print(a,b)

for i in range(n-2):
    print(a+b)
    a,b = b, a+b