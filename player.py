from items import *
from map import *

inventory = [item_phone]

# Changes throughout game, player health, energy, level, and kills.
player_stats = {

	"health": 100,

	"energy": 100,

	"kills": 0,

	"level": ""
}

stats = {
	"stats": player_stats
}

# Start game at Pryzm
current_room = places["Pryzm"]
	
# Game score of user complete.
score = 0

# Is the game still running?
game_running = True

# Max items user can have, modularised.
max_items = 5

# Has the user used a taxi?
dragon = False