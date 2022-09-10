# Made by Noah Liby
# Made for class Computing Fundamentals II (2022FA.CSC.130.0001)
# Made 9/9/20222

def selectionSortDescend(lyst):
    for pos in range(len(lyst)):
        cpos = pos
        for x in range(pos+1, len(lyst)):
            if lyst[cpos] > lyst[x]:
                cpos = x
        (lyst[pos], lyst[cpos]) = (lyst[cpos], lyst[pos])


def main():
    lyst1 = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst1)
    selectionSortDescend(lyst1)
    print("Sorted in descending order:", lyst1)


if __name__ == "__main__":
    main()

