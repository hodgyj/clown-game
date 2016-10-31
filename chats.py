chats = [
    "You chat for a while. How cute",
    "You find out that you both share some common interests.\nWho'd have thought?",
    "You try talking, but they don't respond.",
    "You confess your attraction to them. They suddenly get really awkward.",
    "You try talking about football. It was bad. At least you tried"
]

def print_chat():
    import random
    print(chats[random.randrange(0, len(chats))])