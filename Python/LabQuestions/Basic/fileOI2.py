
def displayWords():
    try:
        with open("demoStudent.txt", "r") as file:
            for line in file:
                words = line.split()  
                short_words = [word for word in words if len(word) < 4]  
                print(" ".join(short_words))  

    except FileNotFoundError:
        print("Error: The file 'demoStudent.txt' does not exist.")


displayWords()