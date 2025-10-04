N = int(input("Enter a number: "))
if N > 1:
    for i in range(2, N//2 + 1):
        if N % 2 == 0:
            print(f'{N} is not a prime number')
            break
    else:
        print(f'{N} is a prime number')
else:
    print(f'{N} is not a prime number')
