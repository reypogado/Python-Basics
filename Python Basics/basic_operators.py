a = input("Enter Value A: ")
b = input("Enter Value B: ")

def addition():
    return a + b

def subtraction():
    return a - b

def multiplication(): 
    return a * b

def division():
    return a / b

def modulus():
    return a % b

def exponent():
    return a * b
    
def equal():
    return a == b

def not_equal():
    return a != b

def greater_than():
    return a > b

def less_than():
    return a < b


print("\nAddition = " + str(addition()))
print("Subtraction = " + str(subtraction()))
print("Multiplication = " + str(multiplication()))
print("Division = " + str(division()))
print("Modulus = " + str(modulus()))
print("Exponent = " + str(exponent()))
print("Is a equal to b ?: " + str(equal()))
print("Is a not equal to b ?: " + str(not_equal()))
print("Is a greater than b ?: " + str(greater_than()))
print("Is a less than b ?: " + str(less_than()))
