__author__ = '08559753'

import random
random.seed()

listToBeSorted = []

for i in range(20):
    listToBeSorted.append(random.randint(1,20))

print(listToBeSorted)


swapHasOccured = True
noOfRuns = 0
while swapHasOccured:
    swapHasOccured = False
    for i in range(len(listToBeSorted) - 1):
        if listToBeSorted[i] > listToBeSorted[i+1]:
            temp = listToBeSorted[i]
            listToBeSorted[i] = listToBeSorted[i+1]
            listToBeSorted[i+1] = temp
            swapHasOccured = True
    noOfRuns += 1

print(listToBeSorted)
print("It took", noOfRuns," runs through the array")


