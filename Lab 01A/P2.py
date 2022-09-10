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

# Get user input
height = gettypefromuser("Enter the height from which the ball is dropped: ", float)
bounce = gettypefromuser("Enter the bounciness index of the ball: ", float)
times = gettypefromuser("Enter the number of times the ball is allowed to continue bouncing: ",int)

# Sets initial values
modheight = height
totalheight = 0

# Does calculation
for x in range((times*2)):
    totalheight += modheight
    if x % 2 == 0: # Every other time lower the modheight. This allows for the "Note that distance traveled for each successive bounce is the distance to the floor plus 0.6 of that distance as the ball comes back up."
        modheight = modheight * bounce
# Prints output
print("\nTotal distance traveled is:",totalheight,"units")