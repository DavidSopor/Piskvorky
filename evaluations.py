from game_field import *

def evaluation():
    c = 0
    while c <1:
        if r1[1] == "X" and r1[2] == "X" and r1[3] == "X":
            print("Player X WON")  
            return True
            break

        elif r2[1] == "X" and r2[2] == "X" and r2[3] == "X":
            print("Player X WON") 
            return True
            break

        elif r3[1] == "X" and r3[2] == "X" and r3[3] == "X":
            print("Player X WON")
            return True
            break

        elif r1[1] == "X" and r2[1] == "X" and r3[1] == "X":
            print("Player X WON")
            return True
            break

        elif r1[2] == "X" and r2[2] == "X" and r3[2] == "X":
            print("Player X WON")
            return True
            break

        elif r1[3] == "X" and r2[3] == "X" and r3[3] == "X":
            print("Player X WON")
            return True
            break

        elif r1[1] == "X" and r2[2] == "X" and r3[3] == "X":
            print("Player X WON")
            return True
            break

        elif r1[3] == "X" and r2[2] == "X" and r3[1] == "X":
            print("Player X WON")
            return True
            break

        elif r1[1] == "O" and r1[2] == "O" and r1[3] == "O":
            print("Player O WON")
            return True
            break
        elif r2[1] == "O" and r2[2] == "O" and r2[3] == "O":
            print("Player O WON")
            return True
            break

        elif r3[1] == "O" and r3[2] == "O" and r3[3] == "O":
            print("Player O WON")
            return True
            break

        elif r1[1] == "O" and r2[1] == "O" and r3[1] == "O":
            print("Player O WON")
            return True
            break

        elif r1[2] == "O" and r2[2] == "O" and r3[2] == "O":
            print("Player O WON")
            return True
            break

        elif r1[3] == "O" and r2[3] == "O" and r3[3] == "O":
            print("Player O WON")
            return True
            break

        elif r1[1] == "O" and r2[2] == "O" and r3[3] == "O":
            print("Player O WON")
            return True
            break

        elif r1[3] == "O" and r2[2] == "O" and r3[1] == "O":
            print("Player O WON")
            return True
            break

        elif r1[1] != "_" and r1[2] != "_" and r1[3] != "_" and r2[1] != "_" and r2[2] != "_" and r2[3] != "_" and r3[1] != "_" and r3[2] != "_" and r3[3] != "_":
            print("DRAW")
            return True
            break
        
        c += 1