from game_field import *
from commands_for_terminal import *


def control_player_x():
    executed = False
    while True:
        if not executed:
            number= get_input()
            executed = True
            
        elif number == 99:
            print("Game ended")
            break

        elif number == 11:
            if r1[1] != "O" and r1[1] =="_":
                r1[1] = "X"
                field()
                break
            elif r1[1] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 12:
            if r1[2] != "O" and r1[2] =="_":
                r1[2] = "X"
                field()
                break
            elif r1[2] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 13:
            if r1[3] != "O" and r1[3] =="_":
                r1[3] = "X"
                field()
                break
            elif r1[3] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 21:
            if r2[1] != "O" and r2[1] =="_":
                r2[1] = "X"
                field()
                break
            elif r2[1] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 22:
            if r2[2] != "O" and r2[2] =="_":
                r2[2] = "X"
                field()
                break
            elif r2[2] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 23:
            if r2[3] != "O" and r2[3] =="_":
                r2[3] = "X"
                field()
                break
            elif r2[3] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 31:
            if r3[1] != "O" and r3[1] =="_":
                r3[1] = "X"
                field()
                break
            elif r3[1] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 32:
            if r3[2] != "O" and r3[2] =="_":
                r3[2] = "X"
                field()
                break
            elif r3[2] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number == 33:
            if r3[3] != "O" and r3[3] =="_":
                r3[3] = "X"
                field()
                break
            elif r3[3] == "X":
                field()
                print()
                print("You already own this place")
                break
            else:
                field()
                print()
                print("This place is owned be enemy")
                break

        elif number != 11 or 12 or 13 or 21 or 22 or 23 or 31 or 32 or 33:
            print()
            field()
            print()
            print("this position doesn't exist")
            break