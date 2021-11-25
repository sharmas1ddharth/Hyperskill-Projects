

a = list(" " * 9)
step = 0
def printgame():
    print('-' * 9)
    for i in range(3):
        print("| {} {} {} |".format(a[0 + 3 * i], a[1 + 3 * i], a[2 + 3 * i]))
    print('-' * 9)
while " " in a:
    playx, playy = input("Enter the coordinates:").split()
    if (int(playx) or int(playy)) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("You should enter numbers!")
    elif (int(playx) or int(playy)) not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
    elif a[(int(playx) - 1) + abs(int(playy) - 3) * 3] != " ":
        print("This cell is occupied! Choose another one!")
    else:
        if step == 0:
            a[(int(playx) - 1) + abs(int(playy) - 3) * 3] = "X"
            step = 1
        elif step == 1:
            a[(int(playx) - 1) + abs(int(playy) - 3) * 3] = "O"
            step = 0
        printgame()
        rule = [a[:3], a[3:6], a[6:], a[0:9:3], a[1:9:3], a[2:9:3], a[0:9:4], a[2:7:2]]
        if ['X', 'X', 'X'] in rule:
            print("X wins")
        elif ['O', 'O', 'O'] in rule:
            print("O wins")
        elif a.count(" ") == 0:
            print("Draw")