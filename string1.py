'''
Author:Nandana Hasheed
Date:29-10-2024
Python program to find vowels in a string
'''
string_input=input("Enter a string")
vowels="aeiouAEIOU"
vowels_count=0
consonants_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
    else:
         consonants_count+=1
print(f"NO of vowels in given string {string_input}={vowels_count}")
print(f"No of consonants in given string{string_input}={consonants_count}")
