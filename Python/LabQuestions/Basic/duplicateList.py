def findDuplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])

    print(f"Duplicate Values: {duplicates}")


numList = [10, 20, 30, 10, 40, 50, 30, 60, 70, 10]
findDuplicates(numList)
