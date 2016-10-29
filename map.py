from items import *
import time
import enemies

map_pryzm = {
	"name": "Pryzm",

	"description": """You stumble out of Pryzm as it closes,
and find yourself on a dark street surrounded
by people near a taxi rank. You prepare
yourself for the long walk home, wishing
the club had stayed open just a little bit longer.
""",

	"exits": {"east" : "Student Union", "west" : "Park"},

	"items": [item_bottle],

	"enemies": [],

	"dead": False,
}

map_park = {
	"name": "Park",

	"description": """You walk through the park, it is
surprisingly quiet with just the sound of owls echoing 
in the distance. There is litter scattered on the
ground and medical equipment is amongst the debris.
There are lights on in the Museum.""" ,

	"descclown": """You can just about make out a shadowy 
shape on the floor ahead of you, it is a large, 
red-wigged clown sinisterly breathing heavily.""",

	"exits": {"west": "Museum", "east": "Museum", "south": "Pryzm"},

	"items": [item_needle],

	"enemies": [enemies.clown_park],

	"dead": False,
}

map_museum = {
	"name": "Museum",

	"description": """You run into the desolate Museum, you can hear
music in the distance, you are safe from the outside world. You stand in
the lobby area and look around... As you turn, a clown appears
from around the corner holding a rusty shiv, and stabs you multiple times
as you beg for your life.""",

	"exits": {},

	"items": [],

	"enemies": [],

	"dead": True,
}

map_lidl = {
	"name": "Lidl",

	"description": """You walk down the dimly lit road towards Lidl.
You see a shotgun lying in the car park, beside the gun there is
smashed glass and a completely empty backpack. You hear laughing
and the sound of rubber balloons squeeling in the dark alley nearby.
""",

	"exits": {"south": "Dark Alley", "west": "Student Union"},

	"items": [item_shotgun],

	"enemies": [],

	"dead": False,
}

map_alley = {
	"name": "Dark Alley",

	"description": """Before you step any further, 3 masked figures
appear from around the corner, dripping in blood. You attempt
to fight back, but their knives are thrusted into your body.
The last thing you see is the bright red noses of the clowns
that murdered you.""",

	"exits": {},

	"items": [],

	"enemies": [],

	"dead": True,
}

map_su = {
	"name": "Student Union",

	"description": """The lights flicker as you enter the SU.
You see a cricket bat lying amongst other dead people scattered 
around the alcohol soaked floor. It is almost silent,
only the droning sound of the wind whistling is apparent.""",
	
	"descclown": """Suddenly, you hear the stomping of enourmous
shoes as a clown comes towards you, as each foot slams down, the clown
laughs and laughs spitting blood everywhere.""",

	"exits": {"east": "Lidl", "west": "Cross Roads"},

	"items": [item_cricket_bat],

	"enemies": [enemies.clown_su],

	"dead": False,
}

map_crossroads = {
	"name": "Cross Roads",

	"description": """You are at the cross roads, everything looks safe and 
not a large pair of shoes in sight. Around you there are a variety of buildings.
There is a letting office, a coffee shop, and the Law & Politics Building.""",

	"descclown": """Standing in the middle of the road, two blood-dripping clowns
have spotted you, as both stare intently at you, they tilt their heads while
perpetually staring at your face and run towards you smiling.""",

	"exits": {"east": "Lidl", "west": "Coffee Shop", "north": "Traffic Lights"},

	"items": [item_bottle, item_bottle],

	"enemies": [enemies.clown_crossroads_1, enemies.clown_crossroads_2],

	"dead": False,
}

map_coffee = {
	"name": "Coffee Shop",

	"description": """You shatter the thick glass of hoffi-coffi
and walk in, carefully trying not to step on the vast amount of
glass laying viciously on the floor. The coffee machine is sat
there switched on with a cup sitting below on the stand.
""",

	"exits": {"south": "Cross Roads"},

	"items": [item_coffee, item_cricket_bat],

	"enemies":[],

	"dead": False,
}

map_traffic = {
	"name": "Traffic Lights",

	"description": """You come to the Traffic Lights and wait
for them turn red and the green man to show, an ironically small
spotty car with a red nose on the bonnet stops.""",
	
	"descclown" : """You start to cross as a seemingly 
endless amount of clowns pour out of the car shouting. 
Finally, the final 15th clown emerges, fighting these
may prove difficult...""",

	"exits": {"south": "Cross Roads", "north": "Empty Road"},

	"items": [item_chocolate],

	"enemies": [enemies.clown_traffic_1, enemies.clown_traffic_2, enemies.clown_traffic_3],

	"dead": False,
}

map_emptyrd = {
	"name": "Empty Road",

	"description": """There are bins scattering litter all up the 
street, you can hear the music coming from the student houses. 
You try to get in one but its locked and no one is replying to
your pleading.""",
	
	"descclown" : """There is a trio of clowns slowly emerging from
certain houses with goliath, size 20 blood-stained shoes. The clowns
scream "I WANT TO DEVOUR YOU" as they walk towards you from different
directions.
""",

	"exits": {"north": "Taly South"},

	"items":[item_bottle],

	"enemies": [enemies.clown_emptyrd_1, enemies.clown_emptyrd_2],

	"dead": False,
}

map_talysouth = {
	"name": "Taly South",

	"description": """You arrive safetly back at your flat and
collapse on the once white bed. As you are about to doze off you notice""",

	"exits": {},

	"items": [],

	"enemies": [],

	"dead": False,
}

places = {
	"Pryzm": map_pryzm,
	"Lidl" : map_lidl,
	"Student Union": map_su,
	"Cross Roads": map_crossroads,
	"Empty Road": map_emptyrd,
	"Coffee Shop": map_coffee,
	"Traffic Lights": map_traffic,
	"Park": map_park,
	"Museum": map_museum,
	"Dark Alley": map_alley,
	"Taly South": map_talysouth,
}
