num = int(input("Enter num: "))
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if num == sum:
   print(num,"is aarmstrong")
else:
   print(num,"is not armstrong")