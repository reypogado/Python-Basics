

def String():
    var = "hello world"
    return var

def multilineStrings():
    var = """Hello World,
        World is round"""
    return var

def stringLength():
    var = "Hello World"
    return len(var)

def stripString():
    var = "Hello World"
    return var.strip()  

def lowerString():
    var = "Hello World"
    return var.lower()

def upperString():
    var = "Hello World"
    return var.upper()

def replaceString():
    var = "Hello World"
    return var.replace("l", "p")

def split():
    var = "Hello, World"
    return var.split(",")

def concantenate():
    var1 = "Hello"
    var2 = "World"
    con = var1 + var2

def stringFormat():
    var = "Hello World"
    return len(var)

print("String: " + str(String()))
print("Multiline String: " + str(multilineStrings()))
print("String Length: " + str(stringLength()))
print("Strip string: " + str(stripString()))
print("Lowercase string " + str(lowerString()))
print("Uppercase String: " + str(upperString()))
print("Replace String: " + str(replaceString()))
print("Split String: " + str(split()))
print("Concantenate String: " + str(concantenate()))
print("Format String: " + str(stringFormat()))


