import sys
from controls_player_x import control_player_x
from controls_player_o import control_player_o
from game_field import *
from evaluations import evaluation



def p1orp2():
    input_string = sys.stdin.readline()
    return int(input_string)

executed = 1

def switcher():
    executed = 0
    print("Select player: X = 1, O = 2")

    while True:
        try:
            if executed < 1:
                number2 = p1orp2()
                if number2 != 1 and number2 != 2:
                    print("Incorrrect number, try again")
                    continue
                executed += 1



            elif evaluation() == True:
                break
            



            elif number2 == 1:
                print()
                print("Player X turn")
                print()
                field()
                control_player_x()           
                number2 = 2


            elif evaluation == True:
                break





            elif number2 == 2:  
                print()          
                print("Player O turn")
                print()
                field()
                control_player_o()
                number2 = 1


        except Exception as e:
            print("Unknown command -> Error:", e)

        
        if evaluation == True:
            break