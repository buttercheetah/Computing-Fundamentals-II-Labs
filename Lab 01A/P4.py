# Written by Noah Liby on 8/16/2022
# For the class 2022FA.CSC.130.0001

p1 = str(input("Player 1: Enter R for rock, P for paper or S for scissors: ")).upper()
p2 = str(input("Player 2: Enter R for rock, P for paper or S for scissors: ")).upper()
if p1 == p2:
    print("Tie")
elif p1 == "P":
    if p2 == "R":
        win = "Player 1"
    elif p2 == "S":
        win = "Player 2"
elif p1 == "R":
    if p2 == "S":
        win = "Player 1"
    elif p2 == "P":
        win = "Player 2"
elif p1 == "S":
    if p2 == "P":
        win = "Player 1"
    elif p2 == "R":
        win = "Player 2"
print(win, "Has won the game!")