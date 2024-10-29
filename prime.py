'''
Author:Nandana Hasheed
Date:29-10-2024
Python program to find prime number
'''
number=int(input("Enter the number"))
isPrime=True
for i in range(2,number//2+1):
    if number%i==0:
        isPrime=False
        break
if isPrime:
    print(f"The give number{number} is prime")
else:
    print(f"The give number{number} is not prime")