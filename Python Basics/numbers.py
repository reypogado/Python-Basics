import random


def int():
    val = 5
    return val
def float():
    val = 1.40
    return val
def complex():
    val = 35e3
    return val

def conversion():
    try:
        val = 2.8
    except ValueError:
        return None
    else:
        return int(val)

def convertToString():
    val = 2.8
    st = str(val)
    return st

def random():
    return random.randrange(1, 10, 10)

# def random():

print("\nint " + str(int()))
print("float: " + str(float()))
print("complex: " + str(complex()))
print("Conversion: " + str(conversion()))
print("Convert to String: " + str(convertToString()))
print("Random: " + str(random()))
# print("Range Function with increment value: " + str(rangeFunctionWithIncrementValue()))
# print("for Loop Else: " + str(forLoopElse()))
# print("nestedLoops: " + str(nestedLoops()))
# print("Pass Statement: " + str(passStatements()))