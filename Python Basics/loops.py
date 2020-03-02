fruits = ["apple" , "banana" , "orange"]
color = ["red" , "green" , "blue"]

def whileLoop():
    i = 1
    st = ""
    while i < len(fruits):
        st+=str(fruits[i])+" "
        i+=1
    return st

def forLoop():  
    st = ""
    for x in fruits:
        st+=x+" "
    return st

def loopString():
    st = ""
    for x in fruits[1]:
        st += x+" "
    return st

def breakStatement():
    st = ""
    for x in fruits:
        st += x+" "
        if x == "banana":
            break
    return st

def continueStatement():
    st = ""
    for x in fruits:
        st += x+" "
        if x == "banana":
            continue
    return st

def rangeFunction():
    st = ""
    for x in range(1,5):
        st += str(x)+" "
    return st

def rangeFunctionWithIncrementValue():
    st = ""
    for x in range(1,6,2):
        st += str(x)+" "
    return st

def forLoopElse():
    st = ""
    for x in fruits:
        st += str(x)+" "
    else:
        st += "End of loop" 
    return st

def nestedLoops():
    st = ""
    for x in fruits:
        for y in color:
            st += str(x) +" is color"+str(y)+" "
    return st

def passStatements():    
    for x in fruits:
        pass

   

print("\nWhileLoop: " + str(whileLoop()))
print("For Loop: " + str(forLoop()))
print("Loop String: " + str(loopString()))
print("Break statement: " + str(breakStatement()))
print("Continue statement: " + str(continueStatement()))
print("Range Function: " + str(rangeFunction()))
print("Range Function with increment value: " + str(rangeFunctionWithIncrementValue()))
print("for Loop Else: " + str(forLoopElse()))
print("nestedLoops: " + str(nestedLoops()))
print("Pass Statement: " + str(passStatements()))