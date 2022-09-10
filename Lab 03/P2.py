# Made by Noah Liby
# Made for class Computing Fundamentals II (2022FA.CSC.130.0001)
# Made 9/9/20222


def reverse(lyst, start, end):
    # Reverses elements in a list, starting from
    # index = start, ending with index = end - 1.
    if end > len(lyst): # Checks if the end is larger than length of list
        print("Ending index cannot be larger than length of list")
        return False # Use return to break function instead of a large else statement. Looks nicer and is easier to read
    elif start >= end: # Checks if start is bigger than end
        print("Starting index must be smaller than ending index")
        return False # Use return to break function instead of a large else statement. Looks nicer and is easier to read
    elif start < 0: # Makes sure start is at least 1
        print("Starting index cannot be smaller than 0")
        return False # Use return to break function instead of a large else statement. Looks nicer and is easier to read
    end = end -1
    rlyst = []
    for i in range(len(lyst)):
        if i >= start and i <= end:
            rlyst.insert(start, lyst[i])
        else:
            rlyst.append(lyst[i])
    return rlyst


def main():
    lyst = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst)
    lyst = reverse(lyst, 0, len(lyst))
    print("Reverse whole list:", lyst)
    lyst = [7, 2, 5, 9, 0, 1]
    lyst = reverse(lyst, 0, 3)
    print("Reverse first 3 elements only:", lyst)
    lyst = [7, 2, 5, 9, 0, 1]
    lyst = reverse(lyst, 1, 5)
    print("Reverse middle 4 elements only:", lyst)
    print("Try to reverse list with starting index = -1 ")
    reverse(lyst, -1, 2)
    print("Try to reverse list with ending index = 7 ")
    reverse(lyst, 0, 7)
    print("Try to reverse list with starting index >= ending index ")
    reverse(lyst, 4, 4)

if __name__ == "__main__":
    main()