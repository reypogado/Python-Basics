class userRegistration:
    def __init__(self, First_name, Last_name, Full_name, Email):
        self.First_name = First_name
        self.Last_name =  Last_name
        self.Full_name = Full_name
        self.Email = Email

users = []
boolean = True

def addUser():
    firstname = str(input("Enter First name: "))
    lastname = str(input("Enter Last name: "))
    fullname = firstname+" "+lastname
    email = str(input("Enter Email: "))    
    user = userRegistration(firstname, lastname, fullname, email)
    users.append(user)
    print("Successfully created user")

def removeUser():
    fullname = str(input("Enter User Full Name to be removed: "))

    
    if checkUserIfExists(fullname):
        for x in range(len(users)):
            if fullname == users[x].Full_name:
                del users[x]
                break
        print("Successfully removed user")
    else:
        print("User does not exist")     

def showUsers():
    st = "Firstname\tLastname\tFullname\tEmail\n\n"
    for x in range(len(users)):
        st += users[x].First_name+"\t\t"+users[x].Last_name+"\t\t"+users[x].Full_name+"\t\t"+users[x].Email+"\n"
    print(st)     
    print(len(users))

def updateUser():
    up = ["firstname","lastname","email"]

    fullname = str(input("Enter User Full Name to be updated: "))
    

    if checkUserIfExists(fullname):
        choice = int(input("""
        Choose what to update
        1. First name
        2. Second name
        3. Email"""))
        update = input("Enter "+str(up[choice-1]))

        for x in range(len(users)):
            if fullname == users[x].Full_name:
                if choice == 1:
                    users[x].First_name = update
                    users[x].Full_name =update+" "+users[x].Last_name
                elif choice == 2:
                    users[x].Last_name = update
                    users[x].Full_name = users[x].First_name+" "+update            
                else:
                    users[x].Email = update
            print("Successfully Updated") 
    else:
        print("User does not exists")
    


def checkUserIfExists(fullname):
    for x in range(len(users)):
        if fullname == users[x].Full_name:
            return True
    return False    

while(boolean):
    choice = input("""
    1. Add User
    2. Show list of users
    3. Remove a user
    4. Update User
    5. Exit""")

    if int(choice) == 1:
        addUser()
    elif int(choice) == 2:
        showUsers()
    elif int(choice) == 3:
        removeUser()
    elif int(choice) == 4:
        updateUser()
    else:    
        boolean = False




