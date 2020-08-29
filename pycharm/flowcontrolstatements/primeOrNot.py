num = int(input("Enter a number to check if it is prime or not : "))
isPrime = True
for x in range(2, num - 1):
    if num % x == 0:
        isPrime = False
if isPrime:
    print("Prime Number")
else:
    print("Not a prime number ")
