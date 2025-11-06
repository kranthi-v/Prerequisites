def isPrime(n):
    if n > 1:
        for i in range(2,n//2+1):
            if n %i==0:
                return False
        else:
            return True
    else:
        return False      
def isReverse(n):
    rev = 0
    while n > 0:
        rem = n%10
        rev = rev*10+rem
        n//=10
    return rev
def paliPrime(LL,UL):
    for n in range(LL,UL+1):
        rev = isReverse(n)
        if rev == n and isPrime(n):
            print(n)
paliPrime(1,50)
