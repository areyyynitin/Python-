
try:
    user = float(input("How much km you have travelled:"))

    if(user < 0):
        print("Invalid")
    elif (user <= 10 ):
        print("Total Amount:" , user*10)
    elif (user <= 20):
        print("Total Amount:" ,user*5)
    else:
        print("Total Amount:" , user*4)
    
except ValueError: 
    print("Invalid Input")