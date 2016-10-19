from map import *
from player import *
from items import *
from gameparser import *
from ascii import *
import random
import sys
import os

def list_of_items(items):
    """This function takes a list of items and returns a comma-separated list of
    item names (as a string).

    >>> list_of_items([item_cricket_bat, item_shotgun])
    'bat, shotgun'

    >>> list_of_items([item_needle])
    'needle'

    >>> list_of_items([])
    ''

    """
    # create new list
    item_list = []

    # for each item in parameter list, add name to new list
    for i in items:
        item_list.append(i["name"])

    # correct list so that each item is seperated by a comma
    correct_list =  ", ".join(item_list)

    return correct_list


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely.

    >>> print_inventory_items(inventory)
    You have: phone.
    <BLANKLINE>

    print_inventory_items()
    --Empty--
    """

    if items:
        print('You have:', list_of_items(items) + ".\n")
    else:
        print('--Empty--')


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room. If there are no items in the room, nothing is printed.

    >>> print_room_items(places["Park"])
    <BLANKLINE>
    There is something here: needle.
    <BLANKLINE>

    >>> print_room_items(places["Coffee Shop"])
    <BLANKLINE>
    There is something here: coffee, bat.
    <BLANKLINE>
    """
    # collect list of items in room
    room_list = list_of_items(room["items"])

    # if list isn't empty list items in room
    if room_list:
        print('\nThere is something here:', room_list + '.\n')


def print_room(room):
    # Prints room the user is in.
    """
    >>> print_room(places["Pryzm"])
    <BLANKLINE>
    -----------------PRYZM------------------
    <BLANKLINE>
    You stumble out of Pryzm as it closes,
    and find yourself on a dark street surrounded
    by people near a taxi rank. You prepare
    yourself for the long walk home, wishing
    the club had stayed open just a little bit longer.
    <BLANKLINE>
    <BLANKLINE>
    You can:
    GO EAST to the Student Union
    GO WEST to the Park
    <BLANKLINE>
    """

    # Display room name
    print('\n' + room["name"].upper() + '\n')
    # Display room description
    print(room["description"] + '\n')

    if room["enemies"] > 0:
        print(room["descclown"] + '\n')


def print_menu(exits, enemies):
    """This function displays the menu of available actions to the player.
    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for enemy in enemies:
        print("FIGHT " + enemies + " clowns")
    print("What do you want to do?")


def exit_leads_to(exits, direction):
   """This function takes a dictionary of exits and a direction. It returns the
   name of the room into which this exit leads.
   """
   return places[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits.

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
        print(new_room)
        current_room = places[new_room]
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory.
    """

    global current_room
    room_item = ""

    # For every item check if user input matches item.
    for item in current_room["items"]:
        if(item["name"] == item_id):
            room_item = item
    # If item is in current room and there is room in inventory for item.
    if room_item and (len(inventory) < 5):
        # Remove item from current room and add to inventory
        current_room["items"].remove(room_item)
        inventory.append(room_item)
    else:
        print("You cannot take that.")


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


def use_weapon(weapon):
    """This function should take a parameter weapon and take 1 point off its health
    as it's being used, it should then check its health and if it's health is 0,
    remove the weapon from inventory and print you won the fight but your weapon broke.
    Else it should just print you won the fight

    >>> use_weapon(item_bottle)
    <BLANKLINE>
    You won the fight, but your weapon broke

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
            del weapon
            print("\nYou won the fight, but your weapon broke")
        else:
            print("\nYou won the fight!")
    else:
        # Not a weapon so print warning.
        print("\nThis is not the time or place to use this!")


def execute_fight():
    """Start fight and output a random picture of clown and player stats.
    For each enemy in room:
    Take off health by random number between 1 and 50.
    Check if weapon in inventory if not, instant lose.
    Choose which weapon to use if there are multiple weapons.
    Weapon health - 1, check if health below 0, if it is remove from inventory and
    print "Weapon broken".
    print "Fight won"
    """

    if clowns:
        fight_sequence()
    else:
        print("\nYou can't fight anything here!\n")


def fight_sequence():
    # call global varibale current_room and print FIGHT
    global current_room
    global max_items

    k = 0
    print("\t\t\tFIGHT")
    # print a random picture of a clown from ascii.py
    clown_rand = random.randrange(1,6)
 
    if clown_rand == 1:
        clown1()
    elif clown_rand == 2:
        clown2()
    elif clown_rand == 3:
        clown3()
    elif clown_rand == 4:
        clown4()
    elif clown_rand == 5:
        clown5()
    elif clown_rand == 6:
        clown6()
 
    print_stats()

    # print the number of enemies to be defeated
    enemies = current_room["enemies"]
    print("You must defeat " + str(enemies) + " clowns. Good Luck.")

    # while there are still enemies to be defeated
    while enemies > 0:
        k += 1
        print("\n\t\t\tFIGHT " + str(k) + "\n")
        list_i = []
        j = 0
        # health -= random.randrange(1,51)
        # print("Lost Health! Health now: " + health)

        # for each item in inventory
        for i in inventory:
            # if it's a weapon add it to the list
            if i["weapon"]:
                list_i.append(i)
                # keep track of how many weapons are in inventory
                j = j + 1

        # if there is only one weapon in inventory
        if j == 1:
            # call use_weapon
            use_weapon(list_i[0])
        # if there are 2 weapons in inventory
        elif j == 2:
            while True:
                # take user input of which weapon they will use
                for i in max_items:
                    # list index i - 1 as count starts 0 not 1
                    list_index = i - 1
                    print(i + ":", str(list_i[list_index]["name"]))

                user_input = input("Which weapon would you like to use?>\t")
                # then call use_weapon with the weapon they chose as the parameter
                if user_input <= max_items and user_input >= 0:
                    use_weapon(list_i[user_input])
                else:
                    print("Please enter a valid number...")
        # if they do not have a weapon in their inventory they die
        else:
            # if they do not have a weapon in their inventory they die
            print("You pat your pockets vigorously but cannot find a weapon. You have died...")
            lose_game()

        player_stats["kills"] += 1

        if (player_stats["health"] <= 0) or (player_stats["energy"] <= 0):
            print("\n\t\tBlood pours out of you as you fall to the ground. You have died...")
            lose_game()
        else:
            enemies = enemies - 1

def execute_run():
    """Take off energy by random number between 30 and 50.
    Define new room as only exit possible or user input.
    current_room = new_room.
    """

    # TAKE AWAY SCORE POINTS?

def execute_command(command):
    """This function takes a command and calls a particular function, depending on
    that command
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
    #elif command[0] == "east" or "west" or "north" or "south":
        #execute_go(command[0])
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
    elif command[0] == "run":
        execute_run()
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
        run - Run away instead of fighting
        inventory/inv - Check the player inventory
        room/items - Check the ground items for a hint
        stats/statistics - Get player statistics like health/exp etc.
            """)
    elif command[0] == "dragon" and current_room["name"] == "Pryzm":
        win_game()
    else:
        print("You murmur words that are incomprehensible...")


def win_game():
    # This is the final print and end game, stops all input but shows high score.

    if condition == "dragon":
        print("""An angelic figure drifts down from the heavens,
            and praises you for finding the easter egg. Sadly,
            you have technically cheated and will not be awarded any points""")
        print("Your score is:", score)
        sys.exit()
    else:
        print("\nCongratulations, you won, your final score was", score + "\n")
        try_again()


def lose_game():
    # If the user dies use this function to trigger options available.
    global score
    global game_running

    # Print ascii for end of game.
    endgame()

    try_again()


def try_again():
    # give user choice to try again.
    print("\n\nWould you like to try again? (Y/N)", score)
    user_choice = input()

    if normalise_input(user_choice) == "N" or normalise_input(user_choice) == "NO":
        game_running == False
        sys.ext()
    elif normalise_input(user_choice) == "Y" or normalise_input(user_choice) == "YES":
        game_running == True
        execfile('game.py')
    else:
        print("Your ghost whispers words that are incomprehensible...")


def menu(exits, room_items, inv_items, enemies):
    """This function prompts the player to type an action.
    The players's input is normalised using the normalise_input()
    function before being returned.
    """
    # Display menu
    print_menu(exits, room_items, inv_items, enemies)
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
    from ascii import title

    print(title)

    if normalised_user_input == "easy":
        stats["stats"]["health"] = 100
        stats["stats"]["energy"] = 100
        stats["stats"]["level"] = "easy"

    elif normalised_user_input == "normal":
        stats["stats"]["health"] = 75
        stats["stats"]["energy"] = 75
        stats["stats"]["level"] = "normal"

    elif normalised_user_input == "hard":
        stats["stats"]["health"] = 50
        stats["stats"]["energy"] = 50
        stats["stats"]["level"] = "hard"

    else:
        print("That was not a valid response, so we put you on easy.")

    while game_running == True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_room_items(current_room)

        if current_room["dead"] == True:
            print("You have died.")
            lose_game()
        elif current_room == places["Taly South"]:
            win_game()
        else:
            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["enemies"])

            # Execute the player's command
            execute_command(command)

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

from player import *
from items import *
from gameparser import *
from ascii import *
import random
import sys
import os

def list_of_items(items):
    """This function takes a list of items and returns a comma-separated list of
    item names (as a string).

    >>> list_of_items([item_cricket_bat, item_shotgun])
    'bat, shotgun'

    >>> list_of_items([item_needle])
    'needle'

    >>> list_of_items([])
    ''

    """
    # create new list
    item_list = []

    # for each item in parameter list, add name to new list
    for i in items:
        item_list.append(i["name"])

    # correct list so that each item is seperated by a comma
    correct_list =  ", ".join(item_list)

    return correct_list


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely.

    >>> print_inventory_items(inventory)
    You have: phone.
    <BLANKLINE>

    print_inventory_items()
    --Empty--
    """

    if items:
        print('You have:', list_of_items(items) + ".\n")
    else:
        print('--Empty--')


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room. If there are no items in the room, nothing is printed.

    >>> print_room_items(places["Park"])
    <BLANKLINE>
    There is something here: needle.
    <BLANKLINE>

    >>> print_room_items(places["Coffee Shop"])
    <BLANKLINE>
    There is something here: coffee, bat.
    <BLANKLINE>
    """
    # collect list of items in room
    room_list = list_of_items(room["items"])

    # if list isn't empty list items in room
    if room_list:
        print('\nThere is something here:', room_list + '.\n')


def print_room(room):
    # Prints room the user is in.
    """
    >>> print_room(places["Pryzm"])
    <BLANKLINE>
    -----------------PRYZM------------------
    <BLANKLINE>
    You stumble out of Pryzm as it closes,
    and find yourself on a dark street surrounded
    by people near a taxi rank. You prepare
    yourself for the long walk home, wishing
    the club had stayed open just a little bit longer.
    <BLANKLINE>
    <BLANKLINE>
    You can:
    GO EAST to the Student Union
    GO WEST to the Park
    <BLANKLINE>
    """

    # Display room name
    print('\n' + room["name"].upper() + '\n')
    # Display room description
    print(room["description"] + '\n')

    if room["enemies"] > 0:
        print(room["descclown"] + '\n')


def print_menu(exits, enemies):
    """This function displays the menu of available actions to the player.
    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for enemy in enemies:
        print("FIGHT " + enemies + " clowns")
    print("What do you want to do?")


def exit_leads_to(exits, direction):
   """This function takes a dictionary of exits and a direction. It returns the
   name of the room into which this exit leads.
   """
   return places[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits.

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
        print(new_room)
        current_room = places[new_room]
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory.
    """

    global current_room
    room_item = ""

    # For every item check if user input matches item.
    for item in current_room["items"]:
        if(item["name"] == item_id):
            room_item = item
    # If item is in current room and there is room in inventory for item.
    if room_item and (len(inventory) < 5):
        # Remove item from current room and add to inventory
        current_room["items"].remove(room_item)
        inventory.append(room_item)
    else:
        print("You cannot take that.")


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


def use_weapon(weapon):
    """This function should take a parameter weapon and take 1 point off its health
    as it's being used, it should then check its health and if it's health is 0,
    remove the weapon from inventory and print you won the fight but your weapon broke.
    Else it should just print you won the fight

    >>> use_weapon(item_bottle)
    <BLANKLINE>
    You won the fight, but your weapon broke

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
            del weapon
            print("\nYou won the fight, but your weapon broke")
        else:
            print("\nYou won the fight!")
    else:
        # Not a weapon so print warning.
        print("\nThis is not the time or place to use this!")


def execute_fight():
    """Start fight and output a random picture of clown and player stats.
    For each enemy in room:
    Take off health by random number between 1 and 50.
    Check if weapon in inventory if not, instant lose.
    Choose which weapon to use if there are multiple weapons.
    Weapon health - 1, check if health below 0, if it is remove from inventory and
    print "Weapon broken".
    print "Fight won"
    """

    if clowns:
        fight_sequence()
    else:
        print("\nYou can't fight anything here!\n")


def fight_sequence():
    # call global varibale current_room and print FIGHT
    global current_room
    global max_items

    k = 0
    print("\t\t\tFIGHT")
    # print a random picture of a clown from ascii.py
    number = random.randrange(1,8)
    print(clowns[number])
    print_stats()

    # print the number of enemies to be defeated
    enemies = current_room["enemies"]
    print("You must defeat " + str(enemies) + " clowns. Good Luck.")

    # while there are still enemies to be defeated
    while enemies > 0:
        k += 1
        print("\n\t\t\tFIGHT " + str(k) + "\n")
        list_i = []
        j = 0
        # health -= random.randrange(1,51)
        # print("Lost Health! Health now: " + health)

        # for each item in inventory
        for i in inventory:
            # if it's a weapon add it to the list
            if i["weapon"]:
                list_i.append(i)
                # keep track of how many weapons are in inventory
                j = j + 1

        # if there is only one weapon in inventory
        if j == 1:
            # call use_weapon
            use_weapon(list_i[0])
        # if there are 2 weapons in inventory
        elif j == 2:
            while True:
                # take user input of which weapon they will use
                for i in max_items:
                    # list index i - 1 as count starts 0 not 1
                    list_index = i - 1
                    print(i + ":", str(list_i[list_index]["name"]))

                user_input = input("Which weapon would you like to use?>\t")
                # then call use_weapon with the weapon they chose as the parameter
                if user_input <= max_items and user_input >= 0:
                    use_weapon(list_i[user_input])
                else:
                    print("Please enter a valid number...")
        # if they do not have a weapon in their inventory they die
        else:
            # if they do not have a weapon in their inventory they die
            print("You pat your pockets vigorously but cannot find a weapon. You have died...")
            lose_game()

        player_stats["kills"] += 1

        if (player_stats["health"] <= 0) or (player_stats["energy"] <= 0):
            print("\n\t\tBlood pours out of you as you fall to the ground. You have died...")
            lose_game()
        else:
            enemies = enemies - 1

def execute_run():
    """Take off energy by random number between 30 and 50.
    Define new room as only exit possible or user input.
    current_room = new_room.
    """

    # TAKE AWAY SCORE POINTS?

def execute_command(command):
    """This function takes a command and calls a particular function, depending on
    that command
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
    #elif command[0] == "east" or "west" or "north" or "south":
        #execute_go(command[0])
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
    elif command[0] == "run":
        execute_run()
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
        run - Run away instead of fighting
        inventory/inv - Check the player inventory
        room/items - Check the ground items for a hint
        stats/statistics - Get player statistics like health/exp etc.
            """)
    elif command[0] == "dragon" and current_room["name"] == "Pryzm":
        win_game()
    else:
        print("You murmur words that are incomprehensible...")


def win_game():
    # This is the final print and end game, stops all input but shows high score.

    if condition == "dragon":
        print("""An angelic figure drifts down from the heavens,
            and praises you for finding the easter egg. Sadly,
            you have technically cheated and will not be awarded any points""")
        print("Your score is:", score)
        sys.exit()
    else:
        print("\nCongratulations, you won, your final score was", score + "\n")
        try_again()


def lose_game():
    # If the user dies use this function to trigger options available.
    global score
    global game_running

    # Print ascii for end of game.
    endgame()

    try_again()


def try_again():
    # give user choice to try again.
    print("\n\nWould you like to try again? (Y/N)", score)
    user_choice = input()

    if normalise_input(user_choice) == "N" or normalise_input(user_choice) == "NO":
        game_running == False
        sys.ext()
    elif normalise_input(user_choice) == "Y" or normalise_input(user_choice) == "YES":
        game_running == True
        execfile('game.py')
    else:
        print("Your ghost whispers words that are incomprehensible...")


def menu(exits, room_items, inv_items, enemies):
    """This function prompts the player to type an action.
    The players's input is normalised using the normalise_input()
    function before being returned.
    """
    # Display menu
    print_menu(exits, room_items, inv_items, enemies)
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
    from ascii import title

    print(title)

    if normalised_user_input == "easy":
        stats["stats"]["health"] = 100
        stats["stats"]["energy"] = 100
        stats["stats"]["level"] = "easy"

    elif normalised_user_input == "normal":
        stats["stats"]["health"] = 75
        stats["stats"]["energy"] = 75
        stats["stats"]["level"] = "normal"

    elif normalised_user_input == "hard":
        stats["stats"]["health"] = 50
        stats["stats"]["energy"] = 50
        stats["stats"]["level"] = "hard"

    else:
        print("That was not a valid response, so we put you on easy.")

    while game_running == True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_room_items(current_room)

        if current_room["dead"] == True:
            print("You have died.")
            lose_game()
        elif current_room == places["Taly South"]:
            win_game()
        else:
            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["enemies"])

            # Execute the player's command
            execute_command(command)

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

    clowns(number)
