def findLargestSmallest(num):
    smallest = num[0]  
    largest = num[0]  

    for i in num:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

    print(f"Smallest Number:" ,smallest)
    print(f"Largest Number:" ,largest )


numList = [12, 45, 2, 67, 34, 89, 1, 23 , 78]
findLargestSmallest(numList)
