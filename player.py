from items import *
from map import *

inventory = [item_phone]

# Needs to be able to change throughout the game, not sure if this will work yet
player_stats = {
	"health": 100,

	"energy": 100,
}

stats = {
	"stats": player_stats
}

# Start game at Pryzm
current_room = places["Pryzm"]

score = 0

game_running = True

max_items = 5