N = int(input("Enter a number: "))
temp = N
rev = 0
while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp//=10
if N == rev:
    print(f'{N} is a palindrome')
else:
    print(f'{N} is not a palindrome')

# string
S = input("Enter the string: ")

if S[::-1] == S:
    print(f'{S} is palindrome')
else:
    print(f'{S} is not palindrome')
