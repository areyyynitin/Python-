try:
    with open("E:\Python\LabQuestions\exception.txt" , "r") as file:
        content = file.read()
        print("File content:" , content)

except FileNotFoundError:
    print("File not found")

