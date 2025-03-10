def countWordsandCase(filename):
    try:
        with open("demoStudent.txt", "r") as file:
            content = file.read()

           
            word_count = len(content.split())

           
            upper_count = sum(1 for char in content if char.isupper())
            lower_count = sum(1 for char in content if char.islower())

            
            print(f"Total Words: {word_count}")
            print(f"Uppercase Letters: {upper_count}")
            print(f"Lowercase Letters: {lower_count}")

    except FileNotFoundError:
        print(f"Error: The file '{demoStudent}' does not exist.")




countWordsandCase("demoStudent.txt")