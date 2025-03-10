def remove(inputString):
    resultString = ""
    seenCharacters = set()
    
    for char in inputString:
        if char not in seenCharacters:
            resultString += char
            seenCharacters.add(char)
    
    return resultString

originalString = input("Enter string: ")
resultantString = remove(originalString)

print("\nOriginal String: ", originalString)
print("String after removing repeated character: ", resultantString)
