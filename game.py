from map import *
from player import *
from items import *
from gameparser import *
from ascii import *
import random
import sys
import sse_python
import time

def sse_send_stats():
#Tell SSE that stats have changed
    sse_python.heartbeat()
    if player_stats["health"] < 0:
        sse_python.send_event("HEALTH", 0)
    else:
        sse_python.send_event("HEALTH", ((player_stats["health"] / player_stats["max_health"]) * 100))

def list_of_items(items):
    """This function takes a list of items and returns a comma sep, list.

    >>> list_of_items([item_cricket_bat, item_shotgun])
    'bat, shotgun'

    >>> list_of_items([item_needle])
    'needle'

    >>> list_of_items([])
    ''
    """

    # Create blank item list to later populate.
    item_list = []

    # For every item in items append with comma.
    for i in items:
        item_list.append(i["name"])

    correct_list =  ", ".join(item_list)

    return correct_list

def print_inventory_items(items):
    """This function takes a list of inventory items and displays nicely.

    >>> print_inventory_items(inventory)
    You have: phone.
    <BLANKLINE>
    """
    
    # Check if any items.
    if items:
        # Create new dict and loop items and add to new list.
        items_list = []

        # For every item in inventory print in list.
        for item in items:
            items_list.append(item["name"])

        print('You have:', ", ".join(items_list) + ".\n")

def print_room_items(room):
    """This function takes a room as an input and prints items in that room.

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

    # Display room name with fancy '-' pattern.
    print('\n' + room["name"].upper().center(50, '-'))

    # Display room description.
    print('\n' + room["description"])

    # If enemies populate room then print clown description for that room.
    if len(room["enemies"]) > 0:
        print('\n' + room["descclown"] + '\n')

def print_menu(exits):
    # Prints available actions to user, apart from fighting (this is optional).

    print("You turn your head hastily, you can")

    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Ask user for input on what they want to do?
    print("\t\nWhat do you want to do?")

def exit_leads_to(exits, direction):
    # Takes dict of exits and a direction they want to go, shows options.

    # Return user options.
    return places[exits[direction]]["name"]

def print_exit(direction, leads_to):
    """ Print user exits.

    For example:
    >>> print_exit("south", "Cross Roads")
    GO SOUTH to Cross Roads.
    """

    print("GO " + direction.upper() + " to " + leads_to + ".")

def execute_go(direction):
    # Move user if valid direction.

    # Call global variable current_room
    global current_room

    # If user defined value is in list of exits from current room...
    if str(direction) in current_room["exits"]:
        # Print name of new room and move to new room
        new_room = current_room["exits"][str(direction)]
        current_room = places[new_room]
    else:
        # Show user that the direction they tried is not valid.
        print("You cannot go there.")

def execute_take(item_id):
    # Take an item if inventory isn't full and item on floor.

    # Get current room
    global current_room

    room_item = ""

    if len(inventory) < 5:
        # For every item check if user input matches item.
        for item in current_room["items"]:
            if(item["id"] == item_id):
                room_item = item
        # If item is in current room and there is room in inventory for item.
        if room_item: 
            # Remove item from current room and add to inventory.
            current_room["items"].remove(room_item)
            inventory.append(room_item)
            print("You take " + str(room_item["name"]) + "\n")
            print(room_item["description"])

            # If item is special, do special energy/health gains!
            if room_item["id"] == "coffee":
                inventory.remove(room_item)
                player_stats["energy"] += 50
                print("You drink the coffee, and gain 50 energy!")
            if room_item["id"] == "chocolate":
                inventory.remove(room_item)
                player_stats["health"] += 30
                if player_stats["health"] > player_stats["max_health"]:
                    player_stats["health"] = player_stats["max_health"]
                print("You unwillingly eat the bounty and gain 30 health!")
        else:
            # Tried to pick up item that doesn't exist potentially.
            print("You cannot take that.")
    else:
        # User inv is full, show this.
        print("Your inventory is full!")

def execute_drop(item_id):
    # Drops item in room user in if input is valid.

    # Get current room.
    global current_room

    # Create blank string to be populated later.
    room_item = ""

    # Loop inventory.
    for item in inventory:
        if(item["name"] == item_id):
            room_item = item
    if room_item:
        # Remove from inventory, add to room.
        inventory.remove(room_item)
        current_room["items"].append(room_item)
    else:
        # Non existent item.
        print("You cannot drop that!")

def print_stats():
    """Take stats from player.py and print them neatly.

    >>> print_stats()
    Your Stats Are:
    <BLANKLINE>
    Health : 100
    Energy : 100
    You have: phone.
    <BLANKLINE>
    """

    # Print user stats.
    print("Your Stats Are:\n" )
    print("Health : " + str(player_stats["health"]))
    print("Energy : " + str(player_stats["energy"]))
    print_inventory_items(inventory)

def score():
    """ To determine the end score. take into account energy and clowns killed

    >>> score()
    200
    """

    # Get user energy and kills.
    e = player_stats["energy"]
    k = player_stats["kills"]

    # determine level game player at and create mutators for score.
    if player_stats["level"] == "hard":
        multi = 3
    elif player_stats["level"] == "normal":
        multi = 2
    else:
        multi = 1

    # Score is energy times 2, add kills times 10, times the effect of the mutator.
    score = ((e * 2)  + (k * 10) * multi)

    # If user used easter egg then no points for them!
    if dragon == True:
        score = 0

    return int(score)

def use_weapon(weapon):
    """ Takes user input based on weapons available, takes damage on weapon.

    >>> use_weapon(item_shotgun)
    <BLANKLINE>
    You won the fight!
    """

    # If weapon exists.
    if weapon["weapon"]:       
        # Taking one point from the weapon's health.
        weapon["health"] -= 1

        # Checking if the health of the weapon is zero or less.
        if weapon["health"] <= 0:
            # If it is removing the weapon from the inventory and printing apppropriate message.
            print("\nYou won the fight, but your weapon is now broken!")
            inventory.remove(weapon)
        else:
            print("\nYou won the fight!")
    else:
        # Not a weapon so print warning.
        print("\nThis is not the time or place to use this!")

def execute_fight():
    # Start fight sequence but check room has clown first.

    # Check room has enemies then run fight sequence, else warning.
    if len(current_room["enemies"]) > 0:
        fight_clowns()
    else:
        print("\nYou can't fight anything here!\n")

def count_weapons(weapon_container = inventory):
    weapon_num = 0
    for item in weapon_container:
        if item["weapon"]:
            weapon_num += 1
    return weapon_num

def fight_clowns():
    # Print intro to the fight (change wording!)
    if len(current_room["enemies"]) > 1:
        print("\nYou square yourself up and prepare to fight \nthe " + str(len(current_room["enemies"])) + " clowns standing in front of you.\n")
    else:
        print("\nYou square yourself up and prepare to fight the clown.\n")
    time.sleep(1)


    # Count number of weapons
    # If they have no weapons, kill them (maybe ask first?)
    if count_weapons() == 0:
        print("Unfortunately, you don't have anything to fight with and promptly die.")
        time.sleep(2)
        lose_game()

    while len(current_room["enemies"]) > 0:

        sse_send_stats() # Send current health to SSE3 for pretty colours

        print("You can: ")
        # For each of the clowns, print their name, current health and strength
        for enemy in current_room["enemies"]:
            print("\tFIGHT " + enemy["name"] + " The Clown (Health: " + str(enemy["health"]) + ", Strength: " + str(enemy["strength"]) + ")")
        print("\tRUN to run from the clowns\n")
        time.sleep(1)
        
        # Player can either RUN to leave the fight or FIGHT the clowns
        # If fight, they must supply the name of the clown (maybe make this clearer?)
        player_input = input("Choose a clown to fight:\t(or you can RUN if you are too scared)\n>\t")
        player_input = normalise_input(player_input) 
        if player_input[0] == "run":
            print("\nYou sprint away as fast as possible, hearing the laughter of clowns as you run.")
            time.sleep(1.2)
            break # Exit while loop, ending the fight
        elif player_input[0] == "fight":
            for enemy in current_room["enemies"]:
                # Check if the name of the enemy matches what the player entered
                # If name does not match, it simply loops round and asks for the name again (could do with notifying the players)
                if enemy["name"].lower() == player_input[1]:
                    continue_fight = True
                    while continue_fight == True:

                        sse_send_stats() # More pretty colours
                        
                        if count_weapons() == 0:
                            # Kill player if they no longer have weapons
                            print("\nYou no longer have any weapons. " + enemy["name"] + " is a very observant clown, so")
                            print("takes this opportunity to kill you.\n")
                            time.sleep(2)
                            lose_game()
                        
                        # Prints all the weapons the player is able to use and asks which weapon to use
                        print("\nChoose a weapon to fight " + enemy["name"] + " with:")
                        for item in inventory:
                            if item["weapon"]:
                                print("\tUSE " + item["id"].upper() + " to use " + item["name"])
                        print("Or, you can type BACK to fight a different clown.")
                        player_input = normalise_input(input(">\t"))
                        if player_input[0] == "back": # Return player to clown selection
                            continue_fight = False
                        elif player_input[0] == "use":
                            for item in inventory:
                                if (item["id"] == player_input[1]):
                                    if item["weapon"]:
                                        # If the item is a weapon, calculate and inflict damage on clown 
                                        # Damage currently calculated by generating a random number between half the 
                                        # item strength and double the item strength
                                        damage = (random.randrange(int(item["strength"] / 2), int(item["strength"] * 2)))
                                        enemy["health"] -= damage
                                        if enemy["health"] < 0:
                                            enemy["health"] = 0 # Set to 0 so it looks better :) 
                                        print("\nYou use " + item["name"] + ", dealing " + str(damage) + " damage.")
                                        time.sleep(0.5)

                                        # Remove health from item and check if it is broken
                                        item["health"] -= 1
                                        if item["health"] <= 0:
                                            print("Your " + item["name"] + " is now broken!")
                                            time.sleep(0.5)
                                            inventory.remove(item) # Remove item from inventory if it is broken

                                        # Print remaining health for the clown
                                        print(enemy["name"] + " has " + str(enemy["health"]) + " HP remaining.")
                                        time.sleep(1)
                                        
                                        # Check if the enemy has been killed
                                        if enemy["health"] <= 0:
                                            print("\nYou killed " + enemy["name"] + " The Clown! You monster.\n")
                                            time.sleep(1)
                                            current_room["enemies"].remove(enemy) # Remove the enemy from the room
                                            player_stats["kills"] += 1
                                            continue_fight = False # Flag to go back to clown selection
                                        else:
                                            # If enemy is alive, calculate and inflict damage on the player 
                                            # Damage calculated by generating a random number between the enemys strength
                                            # and triple the enemys strength
                                            damage = random.randrange(enemy["strength"], enemy["strength"] * 3)
                                            player_stats["health"] -= damage
                                            if player_stats["health"] < 0:
                                                player_stats["health"] = 0 # Set to 0 for prettiness and so that SSE doesnt break
                                            # Print the damage inflicted and remaining HP of the player
                                            print("\n" + enemy["name"] + " retaliated, dealing " + str(damage) + " damage.")
                                            print("You lost " + str(damage) + " HP, leaving you with " + str(player_stats["health"]) + " HP.")
                                            sse_send_stats() # Update SSE so we have pretty colours (before the time delay)
                                            time.sleep(1)
                                            if player_stats["health"] == 0:
                                                # If player is dead, update SSE with health and exit game
                                                sse_send_stats()
                                                print("\n\t\tBlood pours out of you as you fall to the ground, you have died...")
                                                time.sleep(2)
                                                lose_game()
                                            else:
                                                break # Don't loop through multiple items with the same name

                        else:
                            print("That made no sense!")
                    break # Exit for loop
        else:
            print("You can't do that!\n")

def fight_sequence():
    # Start fight code that triggers fighting mechanics.

    global current_room
    global max_items
    
    # Clowns
    k = 0

    # print a random picture of a clown from ascii.py.
    clown_func = random.randint(1,6)
    print_ascii(clowns[clown_func])

    # Print player stats.
    print_stats()

    # print the number of enemies to be defeated.
    print("You must defeat " + str(current_room["enemies"]) + " clowns. Good Luck.")

    # while there are still enemies to be defeated.
    while current_room["enemies"] > 0:
        k += 1
        print("\n\t\tFIGHT " + str(k) + "\n")
        list_i = []
        weapons = 0
        # Take off a small amount of energy and health.
        player_stats["energy"] -= 5
        player_stats["health"] -= random.randrange(1,31)


        # for each item in inventory.
        for i in inventory:
            # if it's a weapon add it to the list.
            if i["weapon"]:
                list_i.append(i)
                # keep track of how many weapons are in inventory.
                weapons = weapons + 1

        # if there is only one weapon in inventory.
        if weapons == 1:
            # call use weapon with only weapon.
            use_weapon(list_i[0])

        elif weapons >= 1:
            while True:
                sse_python.heartbeat()
                # take user input of which weapon they will use.
                for i in range(1, len(inventory)):
                    # list index i - 1 as count starts 0 not 1.
                    list_index = i - 1
                    print(str(i) + ":", str(list_i[list_index]["name"]))

                user_input = input("Which weapon would you like to use?>\t")
                # Use try/catch to try convert to int, if not then they need int.
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
            # if they do not have a weapon in their inventory they die.
            print("""You pat your pockets vigorously but cannot find a weapon, 
The clown smiles slowly as he draws out a blunt knife and thrusts
his hand forward into your chest. You have died...""")
            sse_python.send_event("HEALTH", 0)
            lose_game()

        # Player lost health!
        print("Lost Health! Health now: " + str(player_stats["health"]))
        sse_send_stats()
        player_stats["kills"] += 1

        if player_stats["health"] <= 0 or player_stats["energy"] <= 0:
            print("\n\t\tBlood pours out of you as you fall to the ground, you have died...")
            lose_game()
        else:
            # Player has removed enemy.
            current_room["enemies"] -= 1    

def execute_command(command):
    # Gets user commands, then targets the specific functions required to run commands.
    directions = ["north", "south", "east", "west"]
    if 0 == len(command):
        return
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
    elif command[0] in directions:
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
    elif command[0] == "fight" or command[0] == "fight clown" or command[0] == "clown":
        execute_fight()
    elif command[0] == "inventory" or command[0] == "inv":
        print_inventory_items(inventory)
    elif command[0] == "stats" or command[0] == "statistics":
        print_stats()
    elif command[0] == "help":
        # User requires help, print commands available.
        print("""
        go - Move in a certain direction (eg: "go west")
        take - Take an item from the ground (eg: "take needle")
        drop - Drop an item to make space for another (eg: "drop needle")
        fight/clown/fight clown - Fight an enemy to gain more points/clear area
        inventory/inv - Check the player inventory
        stats/statistics - Get player statistics like health, exp, and inventory
            """)
    elif command[0] == "dragon" and current_room["name"] == "Pryzm":
        # User has cheated/easter egged it.
        global dragon
        dragon = True
        win_game()
    else:
        print("You murmur words that are incomprehensible... Try using 'help' for commands!")

def print_end_dialog(end_dialog_1,end_dialog_2,end_dialog_3):
    # Prints the end dialogs (not sure why they were separated into 3 variables but ah well)
    for i in end_dialog_1:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    for i in end_dialog_2:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    for i in end_dialog_3:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)

def win_game():
    # Account for different win conditions for multiple endings.

    # Dragon easter egg ending.
    if dragon == True:
        print("""\nAn angelic figure drifts down from the heavens and praises you, 
"My name is Kirill, you found the easter egg, good job! Although, you have technically 
cheated, so you will get no points at all."
He then soars back into the heavens, leaving a trail of 0's and 1's behind.\n""")
        print("Your score is:", score())
    # No kill easter egg ending.
    elif player_stats["kills"] == 0:
        enddialogue1 = "needles and pills cover the floor, a belt is wrapped around your arm tightly, "
        enddialogue2 = "you fall to the ground in shock, crying, as you realise you are a drug addict.\n"
        enddialogue3 = "END OF GAME"
        print_end_dialog(enddialogue1, enddialogue2, enddialogue3)
        print("""\nYou decided not to kill anyone, this makes you a drug addict but not
a serial killer, well done - but you have a small score.\n""")
        print("Your score is:", score())
    # Main ending when killed clown and got to final stage.
    else:
        # Standard game win, user killed clowns and didn't get taxi.
        print("""the sound of the doorbell and knocking pierces your ears, 
as you walk out of your door, the hallway is full to the brim
of fully-armoured police labelled "SWAT", they make their way
to you, standing on the once attached front door.
The red dots of the guns stain your body, as they handcuff
you hastily, an officer shouts:""")
        enddialogue1 = "YOU ARE UNDER ARREST FOR THE MASS-MURDER OF MANY INNOCENT PEOPLE ON THE NIGHT OF OCTOBER 31ST AND FOR DISTRIBUTION AND USE OF CLASS A DRUGS. "
        enddialogue2 = "You fall to the ground in shock as you realise that you are the real monster...\n"
        enddialogue3 = "END OF GAME"
        print_end_dialog(enddialogue1, enddialogue2, enddialogue3)
        print("\nCongratulations, you won, your final score was", score())

    # Game has ended user can quit.
    input("\nPress any key to exit and return to reality!")
    exit()

def lose_game():
    # If the user dies use this function to trigger options available and print score.
    print_ascii(endgame)
    player_stats["health"] = 0
    sse_send_stats()
    print("\nYou lost, your final score was", score())
    input()
    exit()

def menu(exits):
    # Get user input, normalise that input to ensure user typos still run.

    print_menu(exits)

    # Read player's input
    user_input = input(">\t")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):
    """This function returns the room into which the player will move.

    >>> move(places["Pryzm"]["exits"], "east") == places["Student Union"]
    True
    >>> move(places["Coffee Shop"]["exits"], "south") == places["Pryzm"]
    False
    """

    # Return next room.
    return places[exits[direction]]

def main():
    try:
        # Main code starts at runtime.

        from map import map_pryzm
        import time
        global current_room



        print_ascii(title)
        # Sleep to show title briefly.
        time.sleep(2)
        print_ascii(clown6)

        # Give user option to play at different levels.
        print("Do you want to play on Easy, Normal, or Hard?")
        user_input = input(">\t")
        normalised_user_input = normalise_input(user_input)
        normalised_user_input = (", ".join(normalised_user_input))

        # User health and energy different for difficulty rating.
        if normalised_user_input == "easy" or normalised_user_input == "e":
            player_stats["health"] = 100
            player_stats["max_health"] = 100
            player_stats["energy"] = 100
            player_stats["level"] = "easy"
        elif normalised_user_input == "normal" or normalised_user_input == "n":
            player_stats["health"] = 75
            player_stats["max_health"] = 75
            player_stats["energy"] = 75
            player_stats["level"] = "normal"
        elif normalised_user_input == "hard" or normalised_user_input == "h":
            player_stats["health"] = 50
            player_stats["max_health"] = 50
            player_stats["energy"] = 50
            player_stats["level"] = "hard"
        else:
            # If user isn't good at typing, give easy!
            print("That was not a valid response, so we put you on easy.")

        # Register game in SSE3
        if sse_python.sse_status():
            print("SSE3 Running")
            sse_python.game_name = "CLOWN-GAME"
            sse_python.game_friendly_name = "Nightmare On Clown St."
            sse_python.register_game(8)
            sse_python.register_event("HEALTH", 0, 100, 1)
            sse_send_stats()

        # Print intial help guide.
        print('\n' + "GUIDE".center(50, '-'))
        print("""\nRemember, you can use the 'help' command at any time!!!!\n
    To start combat use 'fight', then to pick up an object
    use 'take', and 'drop' to remove that object!
    Also, check your items use 'inventory'/'inv', 
    be smart when taking any old item!""")

        while game_running == True:
            sse_python.heartbeat() # Keep SSE running, although it'll die if player takes longer than 15 seconds
            sse_send_stats()
            # Display game status (room description, inventory etc.), main game loop.
            print("")
            print_room(current_room)
            print_room_items(current_room)

            # If went into death room, lose game.
            if current_room["dead"] == True:
                player_stats["health"] = 0
                sse_send_stats()
                lose_game()
            elif current_room == places["Taly South"]:
                # If reached end of map, win game.
                win_game()
            else:
                # Show the menu with possible actions and ask the player.
                command = menu(current_room["exits"])

                # Execute the player's command.
                execute_command(command)
    except KeyboardInterrupt:
        print("Exited.")
        exit()

if __name__ == "__main__":
    import ctypes
    # Change window title.
    ctypes.windll.kernel32.SetConsoleTitleA(b"Nightmare On Clown St.")
    main()
