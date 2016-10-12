#from items import *

place_pryzm = {
	"name": "Pryzym",

	"description": """You stumble out of Pryzym as it closes, and find yourself on a dark street surrounded by people. 
You prepare yourself for the long walk home, wishing Pryzym had stayed open just a little bit longer""",

	"exits": {"east" : "Student Union", "west" : "Park"},

	"items": [item_bottle]
}

places = {
	"Pryzym": place_pryzm
}