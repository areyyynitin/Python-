# Write a python program to reverse a number using a while loop.
   
user = int(input("Enter a number:"))
def reverse(num):
    rem = 0
    while num > 0:
        rem = rem* 10
        rem = rem + num % 10
        num = num // 10
    return rem

print(reverse(user))




