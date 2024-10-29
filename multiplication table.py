'''
Author:Nandana Hasheed
Date:29-10-2024
Python program to print multiplication table upto 12
'''
num=int(input("Enter the number"))
for i in range(1,13):
    mul=num*i
    print(num,"*",i,"\t","=",mul)
