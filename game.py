from map import *
from player import *
from items import *
from gameparser import *
from ascii import *
import random

# def list_of_items(items):
#    """This function takes a list of items (see items.py for the definition) and
#    returns a comma-separated list of item names (as a string). For example:

#    >>> list_of_items([item_cricket_bat, item_shotgun])
#    'a cricket bat, shotgun'

#    >>> list_of_items([item_needle])
#    'a needle'

#    >>> list_of_items([])
#    ''
#    """
    # Create new list
#    list_i = []

    # For item in items add the name of the item to the new list
#    for word in items:
#        list_i.append(word["name"])

    # Format the list so it prints nicely and return the list
#    correct_list =  ", ".join(list_i)

#    return correct_list


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have: phone.
    <BLANKLINE>

    """
    # if items isn't blank...
    if items:
        # create new list
        list_i = []
        # For each item in items add the name of the item to the list
        for item in items:
            list_i.append(item)
        # Then print the list
        print('You have:', ", ".join(list_i) + '.\n')

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. For example:

    >>> print_room(places["Pryzm"])
    <BLANKLINE>
    PRYZM
    <BLANKLINE>
    You stumble out of Pryzym as it closes,
    and find yourself on a dark street surrounded
    by people near a taxi rank. You prepare
    yourself for the long walk home, wishing
    the club had stayed open just a little bit longer.
    Do you want to walk EAST to the Student Union or
    go WEST through the Park?
    <BLANKLINE>

    >>> print_room(places["Lidl"])
    <BLANKLINE>
    LIDL
    <BLANKLINE>
    You walk down the dimly lit road towards Lidl,
    you see a shotgun lying in the car park, beside the gun there is
    smashed glass and a completely empty backpack. You hear laughing
    and the sound of rubber balloons squeeling in the dark alley nearby.
    <BLANKLINE>

    >>> print_room(places["Cross Roads"])
    <BLANKLINE>
    CROSS ROADS
    <BLANKLINE>
    You are at the cross roads, everything looks safe and 
    not a large pair of shoes in sight. Around you there are a variety of buildings.
    There is a letting office, a coffee shop, and the Law & Politics Building. 
    From here there are multiple ways to get home.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print('\n' + room["name"].upper() + '\n')
    # Display room description
    print(room["description"] + '\n')


# def exit_leads_to(exits, direction):
#    """This function takes a dictionary of exits and a direction (a particular
#    exit taken from this dictionary). It returns the name of the room into which
#    this exit leads. For example:

#    >>> exit_leads_to(places["Reception"]["exits"], "south")
#    "MJ and Simon's room"
#    >>> exit_leads_to(places["Reception"]["exits"], "east")
#    "your personal tutor's office"
#    >>> exit_leads_to(places["Tutor"]["exits"], "west")
#    'Reception'
#    """
#    return places[exits[direction]]["name"]``


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
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room or the number of items in inventory is
    larger than or equal to 2, this function prints "You cannot take that."
    """
    # Call global variable current_room
    global current_room

    item = ""

    # Check if user defined item is in current room
    for i in current_room["items"]:
        if i["name"] == item_id:
            item = i

    # If item is in current room and there is room in inventory for item..
    if item and (len(inventory) < 2):
            # Remove item from current room and add to inventory
            current_room["items"].remove(item["name"])
            inventory.append(item)
    else:
        print("You cannot take that.")


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    # call global variable current_room
    global current_room

    # Create new variable item
    item = ""

    # Check if user defined item is in inventory
    for i in inventory:
        if i["name"] == item_id:
            item = i

    # If item is in inventory, remove the item from inventory and
    # add to items in current room
    if item:
        inventory.remove(item)
        current_room["items"].append(item)
    else:
        print("You cannot drop that.")

def print_stats():
    """Take stats from player.py and print them neatly:

    >>> print_stats()
    Your Stats Are:
    <BLANKLINE>
    Health : 100
    Energy : 100
    Inventory : phone
    <BLANKLINE>
    """
    print("Your Stats Are:" + "\n")
    print("Health : " + str(stats["stats"]["health"]))
    print("Energy : " + str(stats["stats"]["energy"]))
    playerinventory = str(inventory)

    no_punct = ""
    for char in playerinventory:
        #checks if each character is punctuation or not
        if not (char in string.punctuation):
            #if the character is not punctuation, it is added to the string no_punct
            no_punct += char

    print("Inventory : " + no_punct)
    print("")

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
    # call global varibale current_room and print FIGHT
    global current_room
    k = 0
    print("\t\t\tFIGHT")
    # print a random picture of a clown from ascii.py
    number = random.randrange(1,8)
    print(clowns[number])
    # print_stats()

    # print the number of enemies to be defeated
    enemies = current_room["enemies"]
    print("You must defeat " + str(enemies) + " clowns. Good Luck.")

    # while there are still enemies to be defeated
    while enemies > 0:
        k += 1
        print("\n\t\t\tFIGHT " + str(k) + "\n")
        list_i = []
        j = 0
#        health -= random.randrange(1,51)
#        print("Lost Health! Health now: " + health)

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
                print("1: " + str(list_i[0]["name"]))
                print("2: " + str(list_i[1]["name"]))
                user_input = input("Which weapon would you like to use? 1 or 2 >\t")
                # then call use_weapon with the weapon they chose as the parameter
                if user_input == "1":
                    use_weapon(list_i[0])
                    break
                elif user_input == "2":
                    use_weapon(list_i[1])
                    break
                else:
                    print("Please enter either 1 or 2.")
        # if they do not have a weapon in their inventory they die
        else:
            print("You do not have a weapon in your inventory. You have died...")
            break
#           end game

#        if health <= 0:
#            print("\t\t\tYou have lost too much health and died...")
        # one enemy has been deafeated
        enemies = enemies - 1


def execute_run():
    """Take off energy by random number between 30 and 50.
    Define new room as only exit possible or user input.
    current_room = new_room.
    """

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

    elif command[0] == "dragon" and current_room["name"] == "Pryzm":
        print("You got home safetly, well done!!!")

    else:
        print("This makes no sense.")


def menu():
    """This function prompts the player to type an action.
    The players's input is normalised using the normalise_input()
    function before being returned.
    """
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
    # Main game loop

    print(title)

    # user_input = input("Do You Want To Play Easy, Normal, Or Difficult?")
    # if user_input == ("easy" or "Easy"):
        # player.health = 100
        # player.energy = 100
    # elif user_input == ("normal" or "Normal"):
        # player.health = 75
        # player.energy = 75
    # elif user_input == ("difficult" or "Difficult"):
        # player.health = 50
        # player.energy = 50
    # else:
        # print("That was not a valid response, so we put you on easy.")

    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu()

        # Execute the player's command
        execute_command(command)

        # Winning game
        #If current_room == places["Taly South"]:
        #    break


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
