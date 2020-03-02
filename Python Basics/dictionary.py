fruits = {
        "name": "apple",
        "color": "red",
        "shape": "circle"
    }

def initializeDictionary():
    fruits = {
        "name": "apple",
        "color": "red",
        "shape": "circle"
    }
    return fruits

def accessDictionary():
    return fruits["name"]

def useGetFunction():
    return fruits.get("name")

def changeValue():
    fruits["name"] = "orange"
    return fruits

def loopThroughDictionary():
    for x in fruits:
        return x

def printAllValues():
    for x in fruits:
        return fruits[x]

def useValuesFunction():
    for x in fruits.values():
        print(x)

def checkifKeyExists():
    if "name" in fruits:
        return true
def dictionaryLength():
    return len(fruits)

def addItems():
    fruits["brand"] = "dairy"
    return fruits


print("\nInitialize Dictionary: " + str(initializeDictionary()))
print("Access Dictionary: " + str(accessDictionary()))
print("Use Get Function: " + str(useGetFunction()))
print("Change Value: " + str(changeValue()))
print("Loop through dictionary: " + str(loopThroughDictionary()))
print("Print all values: " + str(printAllValues()))
print("Use values function: " + str(useValuesFunction()))
print("Check if Key Exists: " + str(checkifKeyExists))
print("Dictionary Length: " + str(dictionaryLength()))
print("Add Items: " + str(addItems()))