a = input("Enter value A: ")
b = input("Enter value B: ")
c = input("Enter value C: ")


def If():
    if a > b:
        return "a is greater than b"

def Elif():
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"

def Else():
    if a > b:
        return "a is greater than b"
    else:
        return "a is not greater than b"

def Elif_With_Else():
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is equal to b"

def Short_Hand_If():
    if a > b: return "a is greater than b"

def Short_Hand_IfElse():
    print("a is greater than b") if a > b else print("a is less than b")

def And():
    if a > b and a > c:
        return "Both are true"

def Or():
    if a > b or a > c:
        return "One condition is true"

def NestedIf(a,b,c):
    if a > b:
        print("a is greater than b")
        if a > c:
            print("and a is greater than c")
        else:
            print("and a is less than c")    

def Pass_Statement():
    if a > b:
        pass



print("\nIf: " + str(If()))
print("Elif: " + str(Elif()))
print("Else: " + str(Else()))
print("Elif with Else: " + str(Elif_With_Else()))
print("Short hand If: " + str(Short_Hand_If()))
print("Short hand IfElse: " + str(Short_Hand_IfElse()))
print("And: " + str(And()))
print("Or: " + str(Or()))
print("Nested If: " + str(NestedIf()))
print("Pass Statement: " + str(Pass_Statement()))