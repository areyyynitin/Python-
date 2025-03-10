tuple1 = (1, 2, 3, 4, 2, 3)
tuple2 = (5, 6, 2, 3 ,4)

newTuple = tuple1 + tuple2  
totalCount = len(newTuple)


repeated = {}
uniqueMem = set(newTuple)

for x in uniqueMem:
    count = newTuple.count(x)
    if count > 1:
        repeated[x] = count


print("New Tuple member:", newTuple)
print("Total member:", totalCount)
print("Repeated memeber:", repeated)
