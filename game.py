from map import *
from player import *
from items import *
from gameparser import *
from ascii import *

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
    You have bottle.
    <BLANKLINE>

    """
    # if items isn't blank...
    if items:
        # create new list
        list_i = []
        # For each item in items add the name of the item to the list
        for item in items:
            list_i.append(item["name"])
        # Then print the list
        print('You have', ", ".join(list_i) + '.\n')

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. For example:

    >>> print_room(rooms["Pryzm"])
    <BLANKLINE>
    PRYZM
    <BLANKLINE>
    You stumble out of Pryzym as it closes,
	and find yourself on a dark street surrounded
	by people near a taxi rank. You prepare
	yourself for the long walk home, wishing
	Pryzm had stayed open just a little bit longer.
	Do you want to walk EAST to the Student Union or
	go WEST through the Park?
    <BLANKLINE>

    >>> print_room(rooms["Lidl"])
    <BLANKLINE>
    LIDL
    <BLANKLINE>
    You walk down the dimly lit road towards Lidl,
	you see a shotgun lying in the car park, you run towards
	it and just as you pick it up, a clown stabs you in the back.
	YOU DIED...
    <BLANKLINE>

    >>> print_room(rooms["Cross Roads"])
    <BLANKLINE>
    CROSS ROADS
    <BLANKLINE>
    You are at the cross roads, everything looks safe,
    there is a Letting Office, a coffee shop and the
    Law and Politics Building. You can go EAST for Lidl
	or NORTH towards the Traffic Lights.
	Which way do you want to walk home?
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

#    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
#    "MJ and Simon's room"
#    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
#    "your personal tutor's office"
#    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
#    'Reception'
#    """
#    return rooms[exits[direction]]["name"]``


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
        current_room = rooms[new_room]
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
    if item and len(inventory) < 2:
            # Remove item from current room and add to inventory
            current_room["items"].remove(item)
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

    # If item is in inventory, remove the item from inventory and add to items in current room
    if item:
        inventory.remove(item)
        current_room["items"].append(item)
    else:
        print("You cannot drop that.")

def print_stats():
    """Take stats from player.py and print them neatly:

    >>> print_stats():
    Health : 100
    Energy : 100
    Inventory : bottle
    """

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

    elif command[0] == "fight"
        execute_fight()

    elif command[0] == "run"
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

    >>> move(rooms["Pryzm"]["exits"], "east") == rooms["Student Union"]
    True
    >>> move(rooms["Cross Roads"]["exits"], "north") == rooms["Traffic Lights"]
    True
    >>> move(rooms["Lidl"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    from map import map_pryzm
    from ascii import title
    # Main game loop

    print(title)

    user_input = input("Do You Want To Play Easy, Normal, Or Difficult?")
    if user_input == ("easy" or "Easy"):
        player.health = 100
        player.energy = 100
    elif user_input == ("normal" or "Normal"):
        player.health = 75
        player.energy = 75
    elif user_input == ("difficult" or "Difficult"):
        player.health = 50
        player.health = 50
    else:
        print("That was not a valid response, so we put you on easy.")

    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu()

        # Execute the player's command
        execute_command(command)

        # Winning game
        If current_room["name"] == "Taly South":
            break


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
