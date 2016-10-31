chats = [
    "You chat for a while. How cute",
    "You find out that you both share some common interests.\nWho'd have thought?",
    "You try talking, but the clown doesn't respond.",
    "You confess your attraction to the clown. They suddenly get really awkward.",
    "You try talking about football. It was bad. At least you tried"
]

def print_chat():
    import random
    print(chats[random.randrange(0, len(chats))])