#Muhsin Maqsood
#New York Institute of Technology
#October 2024

import time
from adventure_package.small_adv_funcs import init_game, inventorychecker, menu, moving, succumb, roomsearcher, inventory

def main_game_runner():
    starttime = init_game()
    running = True
    curroom = "hallway"


    while running:
        option = menu(curroom, int(time.time() - starttime))

        if time.time() - starttime >= 600:
            option = "DEBUG DEATH COMMAND INPUT MADE UNCOPIABLE SO NO PLAYER GUESSES IT"

        if option == "1":
            curroom = moving(curroom)
        elif option == "2":
            roomsearcher(curroom)
        elif option == "3":
            inventorychecker(inventory)
        elif option == "4":
            succumb()
            break
        elif option == "DEBUG DEATH COMMAND INPUT MADE UNCOPIABLE SO NO PLAYER GUESSES IT":
            print("You slowly scramble around the rooms and are sent into a panic as you realize your flame grows weaker and weaker, until it goes out.")
            print("You are left alone in the darkness, but you have hope, maybe in another life you could have beat this trial quickly")
            print("ENDING 2/3: Out of time, Full of hope")
            break
        else:
            print(f"Your grow confused as your try to perform that action, perhaps {option} wasn't a valid input!")


main_game_runner()
