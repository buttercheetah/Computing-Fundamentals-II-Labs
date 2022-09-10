import time
import random
import os
import platform
osv = platform.system()
# a simple function to clear the screen so the interface looks nice
def clearscreen(): 
    if (osv == "Windows"):
        os.system('cls')
    elif (osv == "Linux"):
        os.system('clear')
    elif (osv == "Darwin"):
        os.system('clear')
def printclasses():
    print("Curent Classes: " + str(classes).replace("]", "").replace("[", "").replace("'", "").replace('"', ""))

classes = []
run = True
while run:
    clearscreen()
    printclasses()
    userinput = str(input("Enter A to add course, D to drop course, and E to exit: "))
    if userinput.lower() == "a":
        classes.append(str(input("Enter course to add: ")).upper())
    elif userinput.lower() == "d":
        clearscreen()
        print("Classes currently enrolled: ")
        for n in range(len(classes)):
            print(str(n) + ". " + str(classes[n]))
        print("Please enter either the name or number of the class you wish to drop")
        cd = str(input(": "))
        if cd.isnumeric():
            classes.remove(classes[int(cd)])
        else:
            if cd in classes:
                classes.remove(cd)
            else:
                print("Cannot find class! Please try again")
                time.sleep(2)
    elif userinput.lower() == "e":
        run = False