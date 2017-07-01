import math


def whoIsNext(names, r):
    #Initialize the variables, which hold true if we're working with 5 or less rounds.
    totalValue = len(names)
    previousValue = 0
    lineValue = len(names)
    n = 1
    offset = r - previousValue
    index = offset - 1
    factor = 0
    if r>len(names):
        while totalValue < r:
            #I'll need the previous value to calculate the offset.
            previousValue = len(names) * (2 ** n -1)
            n += 1
            #This gets the total value of how many 'items' are in the queue.
            totalValue = len(names) * (2 ** n -1)
            #This lets me know how deep the current round is.
            lineValue = len(names) * 2 ** (n - 1)
        #This tracks how many times the same person gets another cola
        factor = lineValue//len(names)
        offset = r - previousValue
        #Finally we grab the index!
        index = int(math.ceil(offset/factor))
    return names[index]

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print whoIsNext(names, 52)