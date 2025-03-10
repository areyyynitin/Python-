numbers = (5, 2, 8, 1, 9, 3)

ascSorted = tuple(sorted(numbers))  
reverseSorted = tuple(sorted(numbers, reverse=True))  

print("Original :", numbers)
print("Sorting Ascending:", ascSorted)
print("Sorted Descending:", reverseSorted)
