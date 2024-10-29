'''
Author: Nandana Hasheed
Date:29-10-2024
python program to check whether a number is prime or not
'''
check_prime=int(input("Enter a number"))
for i in range(2,(check_prime)+1):
  if check_prime%i==0:
    break
if i==(check_prime):
    print(f"The given number{check_prime}is prime")
else:
    print(f"The given number{check_prime}is not prime")