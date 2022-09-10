# Made by Noah Liby
# Made for class Computing Fundamentals II (2022FA.CSC.130.0001)
# Made 9/9/20222

# A simple function to return a list as just the contents, no commas or brackets
def ReturnListaAString(l):
    return str(l).replace("[", "").replace("]", "").replace(",", "")

# I dint have to put the bulk of my code in a function, but it was more fun to do that.
def linearSearchSorted(tlist,num):
    elvisited = [] # Defines an empty list
    for i in range(len(tlist)): # Creates a for loop to go over every item in tlist. However, i is not the actual item from the list, instead it is simply a counter
        elvisited.append(tlist[i]) # Append the item to the list so that it can print what items it looked at at the end
        if tlist[i] == num: # If the number is found
            return str("Found at position " + str(i)), ReturnListaAString(elvisited)
        elif tlist[i] > num:# Since this is program is assuming the list is ordered, if the number is higher than the one found, then it does not exist in list
            return "Target no found", ReturnListaAString(elvisited)

my_list = [2, 5, 7, 9, 14, 27]
def main():
    searchTarget = int(input("Search Target "))
    res, visit = linearSearchSorted(my_list, searchTarget)
    print("Elements Visited", visit)
    print(res)

if __name__ == '__main__':
    main()