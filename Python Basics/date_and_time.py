import datetime


month = input("Enter birthmonth: ")
day = input("Enter birthday: ")
year = input("Enter birthyear: ")

dbirth = ""
dtoday = ""


def createDate():
    global dbirth
    dbirth = datetime.datetime(year, month, day)
    return dbirth

def returnYearandDay():
    return str(dbirth.year) +", "+dbirth.strftime("%A")

def yearShortVersion():
    return dbirth.strftime("%y")

def nameOfTheMonth():
    return dbirth.strftime("%B")

def dayNumberInYear():
    return dbirth.strftime("%j")

def localVersion():
    return dbirth.strftime("%c")   

def getDateToday():     
    global dtoday
    dtoday = datetime.datetime.now().date()
    return dtoday

def calculateAge():
    age = dtoday.year - dbirth.year - ((dtoday.month, dtoday.day) < (dbirth.month, dbirth.day))
    return age




print("\nCreate date: " + str(createDate()))
print("Year and Name: " + str(returnYearandDay()))
print("Year short version: " + str(yearShortVersion()))
print("Number of day in year: " + str(dayNumberInYear()))
print("Local Version of date: " + str(localVersion()))
print("Name of the Month: " + str(nameOfTheMonth()))
print("Date Today: " + str(getDateToday())) 
print("Calculate Age: " + str(calculateAge())) 

