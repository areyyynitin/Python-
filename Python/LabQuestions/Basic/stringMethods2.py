def demonstrateStringMethods():
    inputString = input("Enter string: ")

    print("String Methods Demonstration")
    print(f"Original String: '{inputString}'")
    print(f"Replaced 'a' with '@': {inputString.replace('a', '@')}")  
    print(f"Splitted into words: {inputString.split()}")  
    print(f"Joined with '-': {'-'.join(inputString.split())}")  
    


demonstrateStringMethods()
