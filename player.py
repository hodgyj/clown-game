from items import *
from map import *

#Needs to be able to change throughout the game, not sure if this will work yet
player_stats = {
	"health": 100,

	"energy": 100,

	"inventory": [item_bottle["name"]]
}

stats = {
	"stats": player_stats
}

# Start game at Pryzm
current_room = places["Pryzm"]
