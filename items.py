import time

def no_use(in_fight = False):
    print("You can't use that!")
    time.sleep(0.5)

def use_phone(in_fight = False):
    if in_fight:
        print("You take a selfie with the clown. So cute!")
    else:
        print("""\nYou turn on your phone, blinding yourself with the bright screen.
Nice one.""")
    time.sleep(1)

def use_chocolate(in_fight = False):
   
    import player
    print("\nYou eat the bar of chocolate. Tastes like chocolate. What a surprise.")
    time.sleep(0.5)
    player.player_stats["health"] += 30
    if player.player_stats["health"] > player.player_stats["max_health"]:
        player.player_stats["health"] = player.player_stats["max_health"]
    print("Your health is now " + str(player.player_stats["health"]) + ".")
    player.inventory.remove(item_chocolate)
        

item_phone = {
    "id": "phone",
    "name": "your phone",
    "description": """Not much to show here, just an iPhone, 
    not quite sure which one it is though.""",
    "health": 0,
    "strength": 0,
    "weapon": False,
    "use_func": use_phone
}

item_cricket_bat = {
    "id": "bat",
    "name": "a bat",
    "description": """A rugged, wooden cricket bat laying face down with a strange stain beside it.""",
    "health": 10,
    "strength": 5,
    "weapon": True,
    "use_func": no_use
}

item_stick = {
    "id": "stick",
    "name": "a stick",
    "description": """A wooden stick with some concerning stains on it.""",
    "health": 10,
    "strength": 4,
    "weapon": True,
    "use_func": no_use
}

item_shotgun = {
    "id": "shotgun",
    "name": "a shotgun",
    "description": """A slick, matt, black weapon, convieniently placed beside a crammed dustbin that stank of death. 
    This must have been used for something illegal, 
    the gun has been filed down and thoroughly cleaned.""",
    "health": 5, # Why on earth was this 60
    "strength": 10,
    "weapon": True,
    "use_func": no_use
}

item_bottle = {
    "id": "bottle",
    "name": "a bottle",
    "description": """An empty bottle of beer with a an ominous skull and crossbones labelled on the front. 
    These bottles are everywhere, I should keep an eye out, although they do break very easily.""",
    "health": 1,
    "strength": 3,
    "weapon": True,
    "use_func": no_use
}

item_needle = {
    "id": "needle",
    "name": "a needle",
    "description": """A sharp, stained medical needle, laying on the ground beside some bloody bandages.""",
    "health": 1,
    "strength": 1,
    "weapon": True,
    "use_func": no_use
}

item_coffee = {
    "id": "coffee",
    "name": "a cup of coffee",
    "description": """Can't beat a freshly brewed, pumpkin spiced latte during 
    the clown-pocolypse!""",
    "health": 0,
    "strength": 0,
    "weapon": False,
    "use_func": no_use
}

item_chocolate = {
    "id": "chocolate",
    "name": "a bar of chocolate",
    "description": """A bar of bounty, no one likes bounty...""",
    "health": 0,
    "strength": 0,
    "weapon": False,
    "use_func": use_chocolate
}

item_drainpipe = {
    "id": "drainpipe",
    "name": "a drainpipe",
    "description": """A section of drainpipe which fell down about 3 months ago.""",
    "health": 3,
    "strength": 1,
    "weapon": True,
    "use_func": no_use
}

item_mouse = {
    "id": "mouse",
    "name": "a colourful computer mouse",
    "description": """A colourful computer mouse which lights up... preettttyyyy...""",
    "health": 0,
    "strength": 0,
    "weapon": False,
    "use_func": no_use
}

items = {
"coffee": item_coffee,
"needle": item_needle,
"bottle": item_bottle,
"shotgun": item_shotgun,
"cricket bat": item_cricket_bat,
"chocolate": item_chocolate
}
