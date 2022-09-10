# Written by Noah Liby on 8/16/2022
# For the class 2022FA.CSC.130.0001

# Simple function to make sure that the input the type wanted.
def gettypefromuser(text, preferedtype):
    tmpin = ""
    while type(tmpin) != preferedtype:
        tmpin = str(input(text))
        try: tmpin = preferedtype(tmpin)
        except: print("Please only enter "+str(preferedtype)+"!")
    return tmpin

# Gets user input
copies = gettypefromuser("How many copies are you buying? ", int)

# gets unit price
if copies <= 10: unitprice = 99
elif copies <= 50: unitprice = 89
elif copies <= 100: unitprice = 79
else: unitprice = 69

#prints output and does calculation in one line
print("Unit price: $"+ str(unitprice) +"\nTotal price: $" + str(unitprice*copies))