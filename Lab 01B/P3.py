# Function to check if the provided variable can be converted into a float safely
def checkiffloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Function to print a nice table
def makeprettytable(dalist):
    spacing = 10
    for x in dalist:
        tspacing = spacing - len(str(x))
        print(str(x) + str(" " * tspacing),end="")
    print()
        
# Creates an empty list
payroll = []
# Opens file
with open("payroll_data.txt","r") as f:
    # For every line(x) in file(f)
    for x in f:
        # Creates a list(tmp) with the data from the file seperated by a space
        tmp = str(x).replace("\n","").split(" ")
        # For every entry in list try to convert to a number
        for x in range(len(tmp)):
            if tmp[x].isnumeric():
                tmp[x] = int(tmp[x])
            elif checkiffloat(tmp[x]):
                tmp[x] = float(tmp[x])
        # add final product to overall list
        payroll.append(tmp)

# Print everything out
makeprettytable(["Name","Rate","Hours","Total Pay"])
for x in payroll:
    listincludingpay = x.copy()
    listincludingpay.append(listincludingpay[1]*listincludingpay[2])
    makeprettytable(listincludingpay)