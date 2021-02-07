import turtle
import csv

'''
# For loop ======================================================================================================
for steps in range(5):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)


for colours in ['red','blue','purple','brown']:
    turtle.color(colours)
    turtle.forward(100)
    turtle.right(90)


for number in range(1,10,2):
    print(number)

for numbers in [1,67,89,90,56,7]:
    print(numbers)


# While loop =====================================================================================================
answer = "0"
while answer !="4":
    answer = input("What is 2+2? ")  # input always give back string,that's why our initial variable is in quotes.
print("Yea! It's actually 4")


counter = 0
while counter < 5:
    turtle.forward(100)
    turtle.right(90)
    counter +=1


counter = 0
while counter < 5:
    counter +=1
    print(counter)



# list ===========================================================================================================

guest = ['tunde','busayo','taju']
guest.insert(0,'nini')
guest.insert(3,'bibi')
print(guest)

del guest[1]           # deletes by index
print(guest)

guest.remove('nini')    #removes by value
print(guest)

guest.append('Aluwe')
print(guest)
print(guest[-1])


guestList = ['tunji','ayo','taye']
print(len(guestList))
for i in guestList:
    print(i)


guestList = ['tunji','ayo','taye']
del guestList[:]          # empty the list
print(guestList)


guestList2 = ['tunji','ayo','taye', 'funke', 'dami']
numberOfGuests = len(guestList2)
for i in range(numberOfGuests):
    print(guestList2[i])

print() # this empty print function help us create an empty line for readability of our output in the terminal.

#    ALTERNATIVELY
for i in guestList2:
    print(i)

print()

guestList2.sort()
for i in guestList2:
    print(i)
'''

# user enter names of everyone attending the party and print output a list in alphabetical order.
'''list=[]
attend = ' '

while attend != 'X':
    attend = str(input('Please Enter Your name if attending the party: ')).upper()
    list.append(attend)
#list.remove("X")
del list[-1]
list.sort()
for i in attend:
    print(list)
filename ="python demo-microsoft-list.txt"
WRITE ="w"
READ = "r"
READ_WRITE = "w+"    # this reads and write file at the same time.
WRITE_READ = "r+"
APPEND = "a"
myList = open(filename,APPEND)

myList.write(str(list))

myList.close()'''
print("'WRITE' Successful.")

'''# WORKING WITH FILES. How to save information in files ==========================================================
filename ="python demo-microsoft.txt"
WRITE ="w"
READ = "r"
READ_WRITE = "w+"    # this reads and write file at the same time.
WRITE_READ = "r+"
APPEND = "a"
myText = open(filename,WRITE)
myText.write("What is your name?\n")
myText.write("My name is Sylvester.")
myText.close()
print("'WRITE' Successful.")

filename2 ="python demo-microsoft-3.csv"
WRITE ="w"
READ = "r"
READ_WRITE = "w+"    # this reads and write file at the same time.
WRITE_READ = "r+"
APPEND = "a"
fullName = ''
while (fullName and age) != "X":
    fullName = str(input("Please Enter Your Full Name: "))
    formatted = fullName + ','
    age = int(input("Please Enter Your Age: "))
    myCSV = open(filename2,APPEND)
    myCSV.write(formatted)
    myCSV.write(str(age))
    

myCSV.close()
#print("'APPEND' Successful.")

txtFile = open("python demo-microsoft-2.txt","r")
all =txtFile.read()     # read all content
firstRow = txtFile.readline()
print(firstRow)
firstRow = txtFile.readline()
print(firstRow)



#print(all)

with open("python demo-microsoft-2.txt", "r") as myCSVFile:
    useCSV = csv.reader(myCSVFile)
    for i in useCSV:
        #print(i)
        print(",".join(i))      # the use of separators like comma, hyphen to join each row.
        for word in i:
            print(word)


# Function ======================================================================================================

def main():
    guests = getNames()
    printGuestList(guests)
    return



def getNames():
    guests = []
    guestName = ' '
    while guestName != "X":
        guestName = str(input('Enter Guest Name: ')).upper()
        guests.append(guestName)
    del guests[-1]
    guests.sort()
getNames()

def printGuestList(guests):
    for guest in guests:
        print(guest)
    return guest

'''

from DatabaseClass import*

first = DataBase.add_user('syssy@gm.co','guio','syrilo')
first.Database.save()