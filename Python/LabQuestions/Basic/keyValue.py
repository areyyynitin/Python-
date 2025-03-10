dictNum = {1:10,2:20,3:30,4:40,5:50,6:60}

for key in dictNum:
    print("Keys",key)


for key in dictNum:
    print("Values",dictNum[key])


for key,value in dictNum.items():
    print("Key:" , key , ", Value:" , value )
