#Muhsin Maqsood
#New York Institute of Technology
#October 2024

import sys
import time
import random

rnum1 = str(random.randint(1,9))
rnum2 = str(random.randint(1,9))
rnum3 = str(random.randint(1,9))
rnum4 = str(random.randint(1,9))
rnum5 = str(random.randint(1,9))
rnum6 = str(random.randint(1,9))
rnum7 = str(random.randint(1,9))
randomcode = (rnum1 + rnum2 + rnum3 + rnum4 + rnum5 + rnum6 + rnum7)

usedbathkey = False
usedstrangeamulet = False
checkfactor = False
temp = False

inventory = []
rooms = ["hallway", "bedroom", "bathroom", "doorstep", "kitchen", "living room"]

objecthall = ["small desk", "unlit candle", "chandelier"]
objectbed = ["bed", "dirty mirror", "curtains"]
objectbath = ["shattered toilet", "sink", "bathtub"]
objectdoor = ["exit", "doormat"]
objectkit = ["strange breadbox", "dirty dishes", "uneaten food"]
objectlivr = ["couch", "radio", "piano"]

allobjects = [objecthall, objectbath, objectdoor, objectkit, objectlivr, objectbed]

def init_game():
    print("You come to your senses in a mysterious hallway with only an oil candle to guide your path, it seems to have an inscription.")
    tutorial = input("Do you read it? (y/n) (TUTORIAL, HEAVILY RECOMMENDED!): ")

    print("---------------------------------------------------------")

    if tutorial.lower() == "y" or tutorial.lower() == "yes":
        print("You who tread beware, for this lamp only contain enough for thy escape, or thy doom in TEN minutes...")
        print("(This is a timer, after 10 minutes the game will end, the timer will start when the game is started!)")
        print("---")
        print("Try to tread near, there are many ways to escape such a place, death be one of them")
        print("(There are essentially many ways to escape, 4 to be specific, can you find them all?)")
        print("---")
        print("Stab, knock, and inspect all that thy soul shall reveal, to be certain mayhaps all 3 might help thine doomed soul...")
        print("(Using the search action you can stab, knock, or inspect items to gain clues on how to escape or even new items that will help you escape!)")
        print("(INSPECT ALSO USES ITEMS IN YOUR INVENTORY POTENTIALLY TRANSFORMING PREVIOUS UNFRUITFUL SEARCH RESULTS!)")
        print("---")
        print("(When menus have numbers next to the options please type the number (1,2,3,4) as an input, otherwise when formatted like a list ex. ['object1', 'object2', 'object3',] please make sure your input is object1, object2, object3, etc.)")
        print("---------------------------------------------------------")


    tutorial = input("Now that you have come to your senses... do you light the candle and start the trial? (input anything to begin.)")
    print("You light the flame, as you do you realize your fate is sealed, but perhaps you can escape? Only your tenacity can tell...")
    return time.time()

def menu(locroom, loctime):
    print("---------------------------------------------------------")
    print(f"Current room: {locroom}")
    print(f"Current time: {loctime} seconds passed")
    print("---------------------------------------------------------")
    print("1. Move")
    print("2. Search")
    print("3. Check Inventory")
    print("4. Succumb")
    print("---------------------------------------------------------")
    optionloc = input("Choose an option: ")
    return optionloc

def moving(currentroom):
    while True:
        print("---------------------------------------------------------")
        print(f"Rooms: {rooms}")
        print("---------------------------------------------------------")
        room = input("Choose a room by typing its name (q to quit to menu instead): ")
        if room.lower() in rooms:
            canmove = movechecker(room)
            if canmove:
                print(f"You have moved to the {room} from the {currentroom}!")
                descriptionroom(room)
                return room
            else:
                return currentroom
        elif room.lower() == "q":
            print("You quickly change your mind and shake the fear")
            print(f"You stay in the {currentroom}")
            return currentroom
        else:
            print(f"You try to proceed to the {room}, but your search ends up fruitless, perhaps it wasn't a valid room?")


def descriptionroom(room):
    if room.lower() == "bedroom":
        print("You enter into the bedroom, a small quaint room with many lavish wooden furnishings. Your lamp barely illuminates the sullen walls.")

    elif room.lower() == "bathroom":
        print("Entering into the bathroom you are met with the smell of mold that begins to diffuse through the air all around. In front of you is a ruined bathroom with shattered porcelain and mirrors.")

    elif room.lower() == "doorstep":
        print("Approaching the doorstep your tenacity grows as you almost jump and try to rip the door off it's hinges, you could be so close or far from escape, you know that already though don't you?")

    elif room.lower() == "kitchen":
        print("The kitchen now lit by your lamp is a mess of dishes and a small table with various foods and objects on it, looks like someone left mid-meal almost...")

    elif room.lower() == "living room":
        print("Once a room for reading and relaxing now looks like someone died in it, it is dusty and full of cobwebs.")

    elif room.lower() == "hallway":
        print("The place where you awoke, nothing but only a few furnishings here.")

    else:
        print("It seems you have clipped out of the boundaries of this world...")

def succumb():
    print("You look down at your lamp, your shaking hands slowly put it out as you give up to the darkness...")
    print("The darkness closes around you and it consumes you.")
    print("ENDING 1/3: Truly Consumed Ending")

def movechecker(roomtomove):
    if roomtomove.lower() == "bedroom":
        return True

    elif roomtomove.lower() == "bathroom":
        if "bathroom key" in inventory and not usedbathkey:
            print("You use the key you found and it fits into the door perfectly, too perfectly, the key is stuck in the door now, but the door opens to you, so make of that what you will...")
            return True
        elif "bathroom key" in inventory and usedbathkey:
            return True
        else:
            print("You jiggle the handle, but it's locked so you return to whence you came.")
            return False

    elif roomtomove.lower() == "doorstep":
        return True

    elif roomtomove.lower() == "kitchen":
        if "strange amulet" in inventory and not usedstrangeamulet:
            print("The strange amulet on your belt battles away the shadows and clears the fog.")
            return True
        elif "strange amulet" in inventory and usedstrangeamulet:
            return True
        else:
            print("There is a thick fog that clouds the kitchen, the primal energy makes you rush to whence you came, perhaps something supernatural could fight off this fog?")
            return False

    elif roomtomove.lower() == "living room":
        return True

    elif roomtomove.lower() == "hallway":
        return True

    else:
        print("Unfortunately you are not permitted to enter the void")
        return False

def roomsearcher(room):
    print("---------------------------------------------------------")
    print(f"You search around the {room}")

    while True:
        print("---------------------------------------------------------")

        if room.lower() == "bedroom":
            print(f"Items of note: {objectbed}")
            itemtoinspect = input("Please choose an item from above to inspect (q to quit): ")

            if itemtoinspect.lower() in objectbed:
                bedroom_item_manager(itemtoinspect)
            elif itemtoinspect.lower() == "q":
                print("Your lamp flickers and you give up your search...")
                break
            else:
                print(f"You look around unable to find a {itemtoinspect}, perhaps try to find something else or give up...")

        elif room.lower() == "bathroom":
            print(f"Items of note: {objectbath}")
            itemtoinspect = input("Please choose an item from above to inspect (q to quit): ")

            if itemtoinspect.lower() in objectbath:
                bathroom_item_manager(itemtoinspect)
            elif itemtoinspect.lower() == "q":
                print("Your lamp flickers and you give up your search...")
                break
            else:
                print(f"You look around unable to find a {itemtoinspect}, perhaps try to find something else or give up...")

        elif room.lower() == "doorstep":
            print(f"Items of note: {objectdoor}")
            itemtoinspect = input("Please choose an item from above to inspect (q to quit): ")

            if itemtoinspect.lower() in objectdoor:
                doorstep_item_manager(itemtoinspect)
            elif itemtoinspect.lower() == "q":
                print("Your lamp flickers and you give up your search...")
                break
            else:
                print(f"You look around unable to find a {itemtoinspect}, perhaps try to find something else or give up...")

        elif room.lower() == "kitchen":
            print(f"Items of note: {objectkit}")
            itemtoinspect = input("Please choose an item from above to inspect (q to quit): ")

            if itemtoinspect.lower() in objectkit:
                kitchen_item_manager(itemtoinspect)
            elif itemtoinspect.lower() == "q":
                print("Your lamp flickers and you give up your search...")
                break
            else:
                print(f"You look around unable to find a {itemtoinspect}, perhaps try to find something else or give up...")

        elif room.lower() == "living room":
            print(f"Items of note: {objectlivr}")
            itemtoinspect = input("Please choose an item from above to inspect (q to quit): ")

            if itemtoinspect.lower() in objectlivr:
                living_item_manager(itemtoinspect)
            elif itemtoinspect.lower() == "q":
                print("Your lamp flickers and you give up your search...")
                break
            else:
                print(f"You look around unable to find a {itemtoinspect}, perhaps try to find something else or give up...")

        elif room == "hallway":
            print(f"Items of note: {objecthall}")
            itemtoinspect = input("Please choose an item from above to inspect (q to quit): ")

            if itemtoinspect.lower() in objecthall:
                hallway_item_manager(itemtoinspect)
            elif itemtoinspect.lower() == "q":
                print("Your lamp flickers and you give up your search...")
                break
            else:
                print(f"You look around unable to find a {itemtoinspect}, perhaps try to find something else or give up...")

        else:
            print("The void holds no items it seems...")


def bedroom_item_manager(item):
    print("---------------------------------------------------------")
    print(f"You are interacting with the {item}, what do you do?")

    print("---------------------------------------------------------")
    print("1. Stab")
    print("2. Knock")
    print("3. Inspect")
    print("4. Quit")
    print("---------------------------------------------------------")

    if item.lower() == "bed":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print(f"Stabbing the bed with your hand, there appears to be something under the sheets... a paper with the number {rnum1} in red")
                break
            elif action == "2":
                print("Knocking on the sturdy piece of furniture reveals nothing.")
                break
            elif action == "3":
                print(f"Inspecting reveals a paper under the sheets with the number {rnum1} in red")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "dirty mirror":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("You slam your hand into the mirror, cutting it just a bit... probably not a good idea to do that again")
                break
            elif action == "2":
                print("This is a thick mirror as you knock on the glass reflecting your sullen face back")
                break
            elif action == "3":
                if not "strange amulet" in inventory:
                    print("Upon further inspection the mirror is thick and seems like some sort of gateway...")
                elif "strange amulet" in inventory and not "resonating amulet" in inventory:
                    print("The mirror pulls the strange amulet from your pocket and turns into a gateway, its a hole, very deep, but at the bottom a key seems to be placed, but how would one survive the drop? Or even get back up?")
                    print("The amulet begins resonating and clones itself...")
                    print("RESONATING AMULET ACQUIRED")
                    inventory.append("resonating amulet")
                else:
                    print("The gateway remains open...")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "curtains":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("The curtains whip around as you slap them, the view outside is of the void...")
                break
            elif action == "2":
                print("It just seems like you knock on the window behind them")
                break
            elif action == "3":
                if not "resonating amulet" in inventory:
                    print("The curtains seem to be very sturdy and very long as they pile on the floor. It's long enough to be a rope.")
                elif not "void key" in inventory:
                    print("You use the curtains to swing down the hole and retrieve the void key from the mirror gateway, quite odd huh,")
                    print("VOID KEY ACQUIRED")
                    inventory.append("void key")
                else:
                    print("It seems the curtains served their purpose and are tattered now...")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    else:
        print("The item doesn't seem to exist...")

def hallway_item_manager(item):
    print("---------------------------------------------------------")
    print(f"You are interacting with the {item}, what do you do?")

    print("---------------------------------------------------------")
    print("1. Stab")
    print("2. Knock")
    print("3. Inspect")
    print("4. Quit")
    print("---------------------------------------------------------")

    if item.lower() == "small desk":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("Slamming your hand on the side of the desk it almost topples")
                break
            elif action == "2":
                print(f"Knocking around the desk leads to you accidentally opening a hidden compartment, a blue {rnum5} is inscribed within the secret drawer...")
                break
            elif action == "3":
                print("Inspecting reveals a button, you could knock on it?")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "unlit candle":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("The candle topples, it feels wrong, you stand it upright again.")
                break
            elif action == "2":
                print("The candle topples, it feels wrong, you stand it upright again.")
                break
            elif action == "3":
                print(f"Inspecting the candle you realize there is an orange wax {rnum2} attached to the underside of the candle")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "chandelier":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("It's too high to reach...")
                break
            elif action == "2":
                print("It's too high to reach...")
                break
            elif action == "3":
                if "really long knife" in inventory:
                    print("You hit the key off the chandelier with the long knife, quickly picking it up...")
                    print("NICE KEY ACQUIRED")
                    inventory.append("nice key")
                elif "really long knife" in inventory and "nice key" in inventory:
                    print("Just a dusty chandelier...")
                else:
                    print("Upon closer inspection you see a small nice key dangling from the chandelier, you can't reach that high however...")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    else:
        print("The item doesn't seem to exist...")

def bathroom_item_manager(item):
    print("---------------------------------------------------------")
    print(f"You are interacting with the {item}, what do you do?")

    print("---------------------------------------------------------")
    print("1. Stab")
    print("2. Knock")
    print("3. Inspect")
    print("4. Quit")
    print("---------------------------------------------------------")

    if item.lower() == "shattered toilet":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("Stabbing it could injure you gravely, but you do it anyways as the shattered pieces spread")
                break
            elif action == "2":
                print("Knocking on the pieces... you realize they're wet... now you have toilet water on your hands :(")
                break
            elif action == "3":
                print(f"One of the porcelain pieces has a yellow {rnum3} scribbled onto it")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "sink":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("You cringe as your finger crumples upon hitting the sink")
                break
            elif action == "2":
                print("Knocking on the sink reveals nothing")
                break
            elif action == "3":
                print("This sink seems old and used")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "bathtub":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("The bathtub is dirty, now your hand is too :)")
                break
            elif action == "2":
                print("The bathtub is dirty, now your hand is too :)")
                break
            elif action == "3":
                print(f"You wipe away some of the grime revealing a green {rnum4} underneath it.")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    else:
        print("The item doesn't seem to exist...")

def doorstep_item_manager(item):
    print("---------------------------------------------------------")
    print(f"You are interacting with the {item}, what do you do?")

    print("---------------------------------------------------------")
    print("1. Stab")
    print("2. Knock")
    print("3. Inspect")
    print("4. Quit")
    print("---------------------------------------------------------")

    if item.lower() == "exit":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("You feel scared to do that...")
                break
            elif action == "2":
                print("It feels gravely wrong, even more so after the door knocks back...")
                break
            elif action == "3":
                print("You don't wanna look at it for that long at all... all you see is that the door requires 3 keys to open...")
                wingamecond()
                break
            elif action == "4":
                print("You back away, fearful of the door.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "doormat":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("The doormat seems to have something underneath it...?")
                break
            elif action == "2":
                print("The door knocks at you...")
                break
            elif action == "3":
                if not "bathroom key" in inventory:
                    print("A key is underneath the doormat, it says 'bathroom' on it.")
                    print("YOU HAVE ACQUIRED BATHROOM KEY")
                    inventory.append("bathroom key")
                else:
                    print("Just a dusty old carpet, in front of a totally not scary door that makes weird noises... yup totally normal...")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    else:
        print("The item doesn't seem to exist...")

def kitchen_item_manager(item):
    print("---------------------------------------------------------")
    print(f"You are interacting with the {item}, what do you do?")

    print("---------------------------------------------------------")
    print("1. Stab")
    print("2. Knock")
    print("3. Inspect")
    print("4. Quit")
    print("---------------------------------------------------------")

    if item.lower() == "strange breadbox":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("The breadbox doesn't budge...")
                break
            elif action == "2":
                print("It feels as it is forged from the heaviest metals...")
                break
            elif action == "3":
                print("There is a lock with a 7 number combination, on the lock it says 'RAINBOW'. Do you proceed to unlock it?")
                puzzlesolver()
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "dirty dishes":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("Slamming the dirty dishes, some are shattered")
                break
            elif action == "2":
                print("Knocking reveals the fragility of the fine china dishes.")
                break
            elif action == "3":
                if "really long knife" in inventory:
                    print("Just some dirty dishes...")
                else:
                    print("Inspecting reveals a long knife, like really long, among the dishes...")
                    print("LONG KNIFE ACQUIRED")
                    inventory.append("really long knife")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "uneaten food":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("Stabbing down with your hand smashes the food all over the walls...")
                break
            elif action == "2":
                print("Wow your hand is now gross...")
                break
            elif action == "3":
                print("Nothing seems unordinary, its just old uneaten food")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    else:
        print("The item doesn't seem to exist...")

def living_item_manager(item):
    print("---------------------------------------------------------")
    print(f"You are interacting with the {item}, what do you do?")

    print("---------------------------------------------------------")
    print("1. Stab")
    print("2. Knock")
    print("3. Inspect")
    print("4. Quit")
    print("---------------------------------------------------------")

    if item.lower() == "couch":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("Stabbing the couch shocks your hand back as you frantically dash back... what was that???")
                break
            elif action == "2":
                print("Knocking on the soft cushions produces no effect")
                break
            elif action == "3":
                if not "strange amulet" in inventory:
                    print("Inspecting beneath the couch cushions reveals a strange but ominous amulet...")
                    print("STRANGE AMULET ACQUIRED")
                    inventory.append("strange amulet")
                else:
                    print("Just some old coins and gum under the cushions remains now")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "radio":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                if not "sharp antennae" in inventory:
                    print("Stabbing this would surely kill you, the antennae are sharper than climbing picks... maybe remove them?")
                else:
                    print(f"You take your rage out on the previously dangerous radio, now harmless, a violet letter shoots out of the radio as it cracks, it has the number {rnum7} written on it...")
                break
            elif action == "2":
                if "sharp antennae" in inventory:
                    print("Touching this would surely kill you, the antennae are sharper than climbing picks...")
                else:
                    print("Its sturdy... hit it hard enough and it might crack though...")
                break
            elif action == "3":
                if not "sharp antennae" in inventory:
                    print("There are sharp antennae on top of the radio and you don't like it. Carefully removing the sharp antennae on top proves successful... although your not sure of their use...")
                    print("SHARP ANTENNAE ACQUIRED")
                    inventory.append("sharp antennae")
                else:
                    print("A radio without antennae is like a man without a soul... kind of like you am I right?")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    elif item.lower() == "piano":
        while True:
            action = input("Please choose an action from above: ")

            if action == "1":
                print("The piano makes a horrendous noise as you slam the keys")
                break
            elif action == "2":
                print("Knocking on the keys creates a pleasant little musical number")
                break
            elif action == "3":
                print(f"Under the piano cover a indigo {rnum6} is etched")
                break
            elif action == "4":
                print("You back away.")
                break
            else:
                print(f"You try to perform that action to no benefit, perhaps {action} wasn't a valid choice?")
    else:
        print("The item doesn't seem to exist...")

def inventorychecker(inventory):
    num = 0
    if inventory == []:
        print("You check your belt, your pockets, your hands, your eyes! Frantically you realize you have nothing on you... Oh wait you never picked anything up anyways, you calm down...")
    else:
        for item in inventory:
            num += 1
            print(f"{num}. {item}")
        print("That's all you have on your person...")

def puzzlesolver():
    if not "disgusting key" in inventory:
        guess = input("What is the code you input? (Numbers only): ")

        if not guess.isdigit():
            print("Trying to input a letter into the padlock with only numbers was probably where you went wrong...")
        elif not len(guess) == 7:
            print("Last time you checked the padlock had 7 spots to input numbers, you don't think the lock is trying to trick you so you think you should actually input 7 numbers next time...")
        elif guess.isdigit() and guess == randomcode:
            print("The padlock falls off and reveals a disgusting key inside the breadbox...")
            print("DISGUSTING KEY ACQUIRED")
            inventory.append("disgusting key")
        else:
            print("The combination seems to be wrong...")

    else:
        print("The breadbox is open and you already have the key...")


def wingamecond():
    if "disgusting key" in inventory and "nice key" in inventory and "void key" in inventory:
        print("Just as you put the 3 keys into the locks you hear a screech, you don't look back, you jump into the void and end up back in reality!")
        print("ENDING 3/3: Good Ending")
        sys.exit(0)
    else:
        print("You don't have enough keys so you back away...")