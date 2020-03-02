fruits = ["apple", "banana", "orange"]

def initializeLists():
    fruits1 = ["apple", "banana", "orange"]
    return fruits1

def AccessLists():
    return fruits[1]

def NegativeIndexing():
    return fruits[-1]

def rangeIndexes():
    return fruits[1:2]

def negativeRangeIndexes():
    return fruits[-2:-1]

def changeValue():
    fruits[1] = "berry"
    return fruits

def loopThroughLists():
    st = ""
    for x in fruits:
        st+=str(x)+" "
    return st

def checkIfExists():
    if "banana" in fruits:
        return true

def listLength():
    return len(fruits)

def addItem():
    fruits.append("mango")
    return fruits


print("\nInitialize Lists: " + str(initializeLists()))
print("Access Lists " + str(AccessLists()))
print("Negative indexing: " + str(NegativeIndexing()))
print("Range Indexes " + str(rangeIndexes()))
print("Negative range indexes: " + str(negativeRangeIndexes()))
print("Change Item Value: " + str(changeValue()))
print("Loop through Lists: " + str(loopThroughLists()))
print("Check if exists: " + str(checkIfExists()))
print("List length: " + str(listLength()))
print("Add item: " + str(addItem()))