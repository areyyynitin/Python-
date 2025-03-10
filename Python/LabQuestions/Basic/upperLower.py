str = (input("Enter a string: "))
print(str[0])

upr,lwr,num,spl = 0,0,0,0
for i in range(len(str)):
    if(str[i] >= 'A' and str[i] <= 'Z'):
        upr +=1
    elif(str[i] >= 'a' and str[i] <= 'z'):
        lwr +=1
    elif(str[i] >= '0' and str[i] <= '9'):
        num +=1
    else:
        spl +=1

print("Upper case: ",upr)
print("Lower case: ",lwr)
print("Number: ",num)
print("Special char: ",spl)