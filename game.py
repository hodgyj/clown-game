from map import *
from player import *
from items import *
from gameparser import *
from ascii import *
import random
import sys

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_cricket_bat, item_shotgun])
    'bat, shotgun'

    >>> list_of_items([item_needle])
    'needle'

    >>> list_of_items([])
    ''

    """
    item_list = []

    for i in items:
        item_list.append(i["name"])

    correct_list =  ", ".join(item_list)

    return correct_list

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have: phone.
    <BLANKLINE>

    """
    
    # Check if any items.
    if items:
        # Create new dict and loop items and add to new list.
        items_list = []
        for item in items:
            items_list.append(item["name"])
        print('You have:', ", ".join(items_list) + ".\n")

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(places["Park"])
    There is something here: needle.
    <BLANKLINE>

    >>> print_room_items(places["Coffee Shop"])
    There is something here: coffee, bat.
    <BLANKLINE>
    """

    room_list = list_of_items(room["items"])

    if room_list:
        print('There is something here:', room_list + '.\n')

def print_room(room):
    """This function takes a room as an input displays name and description.

    >>> print_room(places["Pryzm"])
    <BLANKLINE>
    ----------------------PRYZM-----------------------
    <BLANKLINE>
    You stumble out of Pryzm as it closes,
    and find yourself on a dark street surrounded
    by people near a taxi rank. You prepare
    yourself for the long walk home, wishing
    the club had stayed open just a little bit longer.
    <BLANKLINE>
    """

    # Display room name
    print('\n' + room["name"].upper().center(50, '-'))
    # Display room description
    print('\n' + room["description"])

    if room["enemies"] > 0:
        print('\n' + room["descclown"] + '\n')

def print_menu(exits):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print
    """
    print("You turn your head hastily, you can")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    print("\t\nWhat do you want to do?")

def exit_leads_to(exits, direction):
   """This function takes a dictionary of exits and a direction (a particular
   exit taken from this dictionary). It returns the name of the room into which
   this exit leads. For example:
   """
   return places[exits[direction]]["name"]

def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    # Call global variable current_room
    global current_room

    # If user defined value is in list of exits from current room...
    if str(direction) in current_room["exits"]:
        # Print name of new room and move to new room
        new_room = current_room["exits"][str(direction)]
        current_room = places[new_room]
    else:
        print("You cannot go there.")

def execute_take(item_id):
    # Take an item if inventory isn't full and item on floor.

    global current_room
    room_item = ""

    if len(inventory) < 5:
        # For every item check if user input matches item.
        for item in current_room["items"]:
            if(item["name"] == item_id):
                room_item = item
        # If item is in current room and there is room in inventory for item.
        if room_item: 
            # Remove item from current room and add to inventory
            current_room["items"].remove(room_item)
            inventory.append(room_item)
            print("You take the " + str(room_item["name"]) + "\n")
            print(room_item["description"])
            if room_item["name"] == "coffee":
                inventory.remove(room_item)
                stats["stats"]["energy"] += 50
                print("You drink the coffee, and gain 50 energy!")
            if room_item["name"] == "chocolate":
                inventory.remove(room_item)
                stats["stats"]["health"] += 30
                print("You unwillingly eat the bounty and gain 30 health!")
        else:
            print("You cannot take that.")
    else:
        print("Your inventory is full!")

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    global current_room

    # Create blank string to be populated later
    room_item = ""

    # Loop inventory
    for item in inventory:
        if(item["name"] == item_id):
            room_item = item
    if room_item:
        # Remove from inventory, add to room.
        inventory.remove(room_item)
        current_room["items"].append(room_item)
    else:
        print("You cannot drop that!")

def print_stats():
    """Take stats from player.py and print them neatly:

    >>> print_stats()
    Your Stats Are:
    <BLANKLINE>
    Health : 100
    Energy : 100
    You have: phone.
    <BLANKLINE>
    """

    # Print user
    print("Your Stats Are:\n" )
    print("Health : " + str(stats["stats"]["health"]))
    print("Energy : " + str(stats["stats"]["energy"]))
    print_inventory_items(inventory)

def score():
    """ To determine the end score. take into account energy and clowns killed

    >>> score()
    200
    """
    e = player_stats["energy"]
    k = player_stats["kills"]

    # determine level game player at
    if player_stats["level"] == "hard":
        multi = 3
    elif player_stats["level"] == "normal":
        multi = 2
    else:
        multi = 1

    # score is energy times 2, add kills times 10, times the effect of the level
    score = ((e * 2)  + (k * 10) * multi)

    if dragon == True:
        score = 0

    return int(score)

def use_weapon(weapon):
    """This function should take a parameter weapon and take 1 point off its health
    as it's being used, it should then check its health and if it's health is 0,
    remove the weapon from inventory and print you won the fight but your weapon broke.
    Else it should just print you won the fight
    
    >>> use_weapon(item_shotgun)
    <BLANKLINE>
    You won the fight!
    """
    if weapon["weapon"]:       
        # Taking one point from the weapon's health
        weapon["health"] -= 1

        # Checking if the health of the weapon is zero
        if weapon["health"] <= 0:
            # If it is removing the weapon from the inventory and printing apppropriate
            print("\nYou won the fight, but your weapon broke")
            inventory.remove(weapon)
        else:
            print("\nYou won the fight!")
    else:
        # Not a weapon so print warning.
        print("\nThis is not the time or place to use this!")

def execute_fight():
    # Start fight but check room has clown first.

    if current_room["enemies"] > 0:
        fight_sequence()
    else:
        print("\nYou can't fight anything here!\n")

def fight_sequence():
    # Start fight code that triggers fighting mechanics.

    global current_room
    global max_items
    
    # Clowns
    k = 0

    # print a random picture of a clown from ascii.py
    clown_func = random.randint(1,6)
    if clown_func == 1:
        clown1()
    if clown_func == 2:
        clown2()
    if clown_func == 3:
        clown3()
    if clown_func == 4:
        clown4()
    if clown_func == 5:
        clown5()

    print_stats()

    # print the number of enemies to be defeated
    print("You must defeat " + str(current_room["enemies"]) + " clowns. Good Luck.")

    # while there are still enemies to be defeated
    while current_room["enemies"] > 0:
        k += 1
        print("\n\t\tFIGHT " + str(k) + "\n")
        list_i = []
        weapons = 0
        player_stats["energy"] -= 5
        player_stats["health"] -= random.randrange(1,31)

        # for each item in inventory
        for i in inventory:
            # if it's a weapon add it to the list
            if i["weapon"]:
                list_i.append(i)
                # keep track of how many weapons are in inventory
                weapons = weapons + 1

        # if there is only one weapon in inventory
        if weapons == 1:
            # call use weapon with only weapon
            use_weapon(list_i[0])

        elif weapons >= 1:
            while True:
                # take user input of which weapon they will use
                for i in range(1, len(inventory)):
                    # list index i - 1 as count starts 0 not 1
                    list_index = i - 1
                    print(str(i) + ":", str(list_i[list_index]["name"]))

                user_input = input("Which weapon would you like to use?>\t")
                # Use try/catch to try convert to int, if not then they need int
                try: 
                    user_input = int(user_input)
                    if user_input <= (len(inventory) - 1) and user_input > 0:
                        use_weapon(list_i[(int(user_input)-1)])
                        break
                    else:
                        print("enter a number from the list!")
                except ValueError:
                    print("Please enter a valid number...")
        else:
            # if they do not have a weapon in their inventory they die
            print("""You pat your pockets vigorously but cannot find a weapon, 
The clown smiles slowly as he draws out a blunt knife and thrusts
his hand forward into your chest. You have died...""")
            lose_game()

        print("Lost Health! Health now: " + str(player_stats["health"]))
        player_stats["kills"] += 1

        if player_stats["health"] <= 0 or player_stats["energy"] <= 0:
            print("\n\t\tBlood pours out of you as you fall to the ground, you have died...")
            lose_game()
        else:
            current_room["enemies"] -= 1    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", "drop", "fight", "run", or "dragon"), executes
    either execute_go, execute_take, execute_drop, execute_fight, or execute_run,
    supplying the second word as the argument if the function requires one.
    """

    if 0 == len(command):
        return
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
    elif command[0] == "east":
        if len(command) == 1:
            execute_go(command[0])
    elif command[0] == "west":
        if len(command) == 1:
            execute_go(command[0])
    elif command[0] == "north":
        if len(command) == 1:
            execute_go(command[0])
    elif command[0] == "south":
        if len(command) == 1:
            execute_go(command[0])
    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "fight":
        execute_fight()
    elif command[0] == "fight clown":
        execute_fight()
    elif command[0] == "inventory" or command[0] == "inv":
        print_inventory_items(inventory)
    elif command[0] == "stats" or command[0] == "statistics":
        print_stats()
    elif command[0] == "help":
        print("""
        go - Move in a certain direction (eg: "go west")
        take - Take an item from the ground (eg: "take needle")
        drop - Drop an item to make space for another (eg: "drop needle")
        fight - Fight an enemy to pass area
        inventory/inv - Check the player inventory
        room/items - Check the ground items for a hint
        stats/statistics - Get player statistics like health/exp etc.
            """)
    elif command[0] == "dragon" and current_room["name"] == "Pryzm":
        global dragon
        dragon = True
        win_game()
    else:
        print("You murmur words that are incomprehensible... Try using 'help' for commands!")

def win_game():
    if dragon == True:
        print("""\nAn angelic figure drifts down from the heavens and praises you, 
"My name is Kirill, you found the easter egg, good job! Although, you have technically 
cheated, so you will get no points at all."
He then soars back into the heavens, leaving a trail of 0's and 1's behind.\n""")
        print("Your score is:", score())
    elif stats["stats"]["kills"] == 0:
        enddialogue1 = "needles and pills cover the floor, a belt is wrapped around your arm tightly, "
        enddialogue2 = "you fall to the ground in shock, crying, as you realise you are a drug addict.\n"
        enddialogue3 = "END OF GAME"
        for i in enddialogue1:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        for i in enddialogue2:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        for i in enddialogue3:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        print("""\nYou decided not to kill anyone, this makes you a drug addict but not
a serial killer, well done - but you have a small score.\n""")
        print("Your score is:", score())
    else:
                # no arg - standard win of game.
        print("""the sound of the doorbell and knocking pierces your ears, 
    as you walk out of your door, the hallway is full to the brim
    of fully-armoured police labelled "SWAT", they make their way
    to you, standing on the once attached front door.
    The red dots of the guns stain your body, as they handcuff
    you hastily, an officer shouts:  
            """)
        enddialogue1 = "YOU ARE UNDER ARREST FOR THE MASS-MURDER OF MANY INNOCENT PEOPLE ON THE NIGHT OF OCTOBER 31ST AND FOR DISTRIBUTION AND USE OF CLASS A DRUGS. "
        enddialogue2 = "You fall to the ground in shock as you realise that you are the real monster...\n"
        enddialogue3 = "END OF GAME"
        for i in enddialogue1:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        for i in enddialogue2:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        for i in enddialogue3:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        print("\nCongratulations, you won, your final score was", score())

    input("\nPress any key to exit and return to reality!")
    sys.exit()

def lose_game():
    # If the user dies use this function to trigger options available.
    endgame()
    print("\nYou lost, your final score was", score())
    input()
    sys.exit()

def menu(exits):
    """This function prompts the player to type an action.
    The players's input is normalised using the normalise_input()
    function before being returned.
    """
    print_menu(exits)

    # Read player's input
    user_input = input(">\t")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(places["Pryzm"]["exits"], "east") == places["Student Union"]
    True
    >>> move(places["Cross Roads"]["exits"], "north") == places["Traffic Lights"]
    True
    >>> move(places["Coffee Shop"]["exits"], "south") == places["Pryzm"]
    False
    """
    # Next room to go to
    return places[exits[direction]]

# This is the entry point of our program
def main():
    global current_room
    from map import map_pryzm
    title()
    clown6()

    print("Do you want to play on Easy, Normal, or Hard?")
    user_input = input()
    normalised_user_input = normalise_input(user_input)
    normalised_user_input = (", ".join(normalised_user_input))

    if normalised_user_input == "easy":
        stats["stats"]["health"] = 100
        stats["stats"]["energy"] = 100
        player_stats["level"] = "easy"
    elif normalised_user_input == "normal":
        stats["stats"]["health"] = 75
        stats["stats"]["energy"] = 75
        player_stats["level"] = "normal"
    elif normalised_user_input == "hard":
        stats["stats"]["health"] = 50
        stats["stats"]["energy"] = 50
        player_stats["level"] = "hard"
    else:
        print("That was not a valid response, so we put you on easy.")

    while game_running == True:
        # Display game status (room description, inventory etc.)
        print("")
        print_room(current_room)
        print_room_items(current_room)

        if current_room["dead"] == True:
            lose_game()
        elif current_room == places["Taly South"]:
            win_game()
        else:
            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"])

            # Execute the player's command
            execute_command(command)

if __name__ == "__main__":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleA(b"Nightmare On Clown St.")
    main()
