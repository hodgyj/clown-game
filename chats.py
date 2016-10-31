chats = [
    "You chat for a while. How cute",
    "You find out that you both share some common interests.\nWho'd have thought?",
    "You try talking, but they don't respond.",
    "You confess your attraction to them. They suddenly get really awkward.",
    "You try talking about football. It was bad. At least you tried",
    "You tell a joke about clowns. \nThey laugh uncontrollably. \nYou feel uncomfortable.",
    "You find out you both like eating meat. \nAt least thats something you have in common. \nNow why are they looking at you like that...",
    "You ask them where they get their shoes. They stare at you.",
    "You ask them if they come here often. They don't respond. \nYou feel embarressed.",
    "You talk about the weather for a while. It's cold.",
    "You ask for them to tell you a joke. They laugh. You're not sure why...",
    "You ask for directions. They look confused."
    "You try talking, but their heavy breathing is putting you off. \nYou stop trying."
]

def print_chat():
    import random
    print(chats[random.randrange(0, len(chats))])