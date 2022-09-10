# Written by Noah Liby on 8/16/2022
# For the class 2022FA.CSC.130.0001

# Simple function to make sure that the input is only a float.
def gettypefromuser(text, preferedtype):
    tmpin = ""
    while type(tmpin) != preferedtype:
        tmpin = str(input(text))
        try: tmpin = preferedtype(tmpin)
        except: print("Please only enter "+str(preferedtype)+"!")
    return tmpin

# Gets input from user
hourlywage = gettypefromuser("Enter hourly wage: $", float)
regularhours = gettypefromuser("Enter regulat hours: ", float)
overtime = gettypefromuser("Enter the overtime hours: ", float)

# Does calculation
total = (hourlywage * regularhours) + ((hourlywage * 1.5) * overtime)

# Prints output
print("The total weekly pay is $" + str(total))