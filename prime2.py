'''
Author:Nandana Hasheed
Date:29-10-2024
python program to find n prime numbers
'''
limit=int(input("Enter the limit"))
for limit in range(2,limit+1):
    isPrime=True
    for i in range(2,(limit//2)+1):
        if limit%i==0:
           isPrime=False
    if isPrime:
       print(limit,end=" ")