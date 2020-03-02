fruits = ("apple", "banana", "orange")

def initializeTuples():
    fruits = ("apple", "banana", "orange")
    return fruits

def accessTuples():
    return fruits[1]

def combineTuples():
    tuple1 = ("a","b","c")
    tuple2 = ("e","f","g")
    add = tuple1 + tuple2
    return add

def NegativeRangeIndexes():
    return fruits[-2:-1]

def loopThroughTuple():
    st = ""
    for x in fruits:
        st+=str(x)+" "
    return st

def checkIfExists():
    if "banana" in fruits:
        return "true"

def tupleLength():
    return len(fruits)

def negativeIndexing():
    return fruits[-1]

def rangeIndexes():
    return fruits[1:2]

def deleteTuple():
    del fruits

print("\nInitialize tuples " + str(initializeTuples()))
print("Access tuples " + str(accessTuples()))
print("Combine tuples: " + str(combineTuples()))
print("Negative range indexes: " + str(NegativeRangeIndexes()))
print("Loop through tuples: " + str(loopThroughTuple()))
print("Check if Exists: " + str(checkIfExists()))
print("Tuples Length: " + str(tupleLength()))
print("Negative indexing: " + str(negativeIndexing()))
print("Range Indexes: " + str(rangeIndexes()))


