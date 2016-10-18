from items import *

map_pryzm = {
	"name": "Pryzm",

	"description": """You stumble out of Pryzm as it closes,
and find yourself on a dark street surrounded
by people near a taxi rank. You prepare
yourself for the long walk home, wishing
the club had stayed open just a little bit longer.
\n
You can:
GO EAST to the Student Union
Go WEST to the Park""",

	"exits": {"east" : "Student Union", "west" : "Park"},

	"items": [item_bottle],

	"enemies": 0,

	"dead": False,
}

map_park = {
	"name": "Park",

	"description": """You walk through the park, it is
surprisingly quiet with just the sound of owls echoing 
in the distance, there is litter scattered on the
ground, a needle is amongst the debris.
There are lights on in the Museum, you can just about
make out a shadowy shape on the floor ahead of you, it 
is a large red-wigged clown, breathing heavily.
\n
You can:
GO EAST or WEST to the Museum""",

	"exits": {"west": "Museum", "east": "Museum"},

	"items": [item_needle],

	"enemies": 1,

	"dead": False,
}

map_museum = {
	"name": "Museum",

	"description": """You run into the desolate Museum, you can hear
music in the distance, you are safe from the clown. You stand in
the lobby area and look around... As you turn, a clown appears
from around the corner holding a rusty shiv, and stabs multiple
as you beg for your life. You have died...""",

	"exits": {},

	"items": [],

	"enemies": 0,

	"dead": True,
}

map_lidl = {
	"name": "Lidl",

	"description": """You walk down the dimly lit road towards Lidl,
you see a shotgun lying in the car park, beside the gun there is
smashed glass and a completely empty backpack. You hear laughing
and the sound of rubber balloons squeeling in the dark alley nearby.
\n
You can:
GO SOUTH to a Dark Alley
GO WEST to the Student Union""",

	"exits": {"south": "Dark Alley", "west": "Student Union"},

	"items": [item_shotgun],

	"enemies": 0,

	"dead": False,
}

map_alley = {
	"name": "Dark Alley",

	"description": """Before you step any further, 3 masked figures
appear from around the corner, dripping in blood. You attempt
to fight back, but the knife slowly is pulled out of your body.
The last thing you see is the bright red noses of the clowns
that murdered you. You have died...""",

	"exits": {},

	"items": [],

	"enemies": 0,

	"dead": True,
}

map_su = {
	"name": "Student Union",

	"description": """The lights flicker as you enter the SU,
you see a cricket bat lying amongst other dead people scattered 
around the alcohol soaked floor. It is almost silent,
only the droning sound of the wind whistling is apparent. Suddenly,
you hear the stomping of enourmous shoes as a clown comes towards you.
\n
You can:
FIGHT the Clown
GO EAST to Lidl
GO WEST to Cross Roads""",

	"exits": {"east": "Lidl", "west": "Cross Roads"},

	"items": [item_cricket_bat],

	"enemies": 0,

	"dead": False,
}

map_crossroads = {
	"name": "Cross Roads",

	"description": """You are at the cross roads, everything looks safe and 
not a large pair of shoes in sight. Around you there are a variety of buildings.
There is a letting office, a coffee shop, and the Law & Politics Building. 
From here there are multiple ways to get home, but standing in the middle of the road, 
two clowns have spotted you.
\n
You can:
FIGHT the Clown
GO NORTH to Traffic Lights
GO EAST to Lidl
GO WEST to Coffee Shop""",

	"exits": {"east": "Lidl", "west": "Coffee Shop", "north": "Traffic Lights"},

	"items": [item_bottle, item_bottle],

	"enemies": 0,

	"dead": False,
}

map_coffee = {
	"name": "Coffee Shop",

	"description": """You shatter the thick glass of hoffi-coffi
and walk in, carefully trying not to step on the vast amount of
glass laying viciously on the floor. The coffee machine is sat
there, switched on with a cup sitting below on the stand.
\n
You can:
GO SOUTH to Cross Roads""",

	"exits": {"south": "Cross Roads"},

	"items": [item_coffee, item_cricket_bat],

	"enemies":0,

	"dead": False,
}

map_traffic = {
	"name": "Traffic Lights",

	"description": """You come to the Traffic Lights and wait
for them turn red and the green man to show, a ironically small
spotty car with a red nose on the bonnet stops. You start to 
cross as a seemingly perpetual amount of clowns pour out of the 
car. Finally the 10th and last clown emerges, fighting these
may prove difficult...
\n
You can:
FIGHT the Clowns
GO NORTH to Taly South
Go SOUTH to Cross Roads""",

	"exits": {"south": "Cross Roads", "North": "Taly South"},

	"items": [],

	"enemies":10,

	"dead": False,
}

map_emptyrd = {
	"name": "Empty Road",

	"description": """There are bins scattering litter all up the 
street, you can hear the music coming from the student houses. 
You try to get in one but its locked and no one is replying to
your pleading. There is a trio of clowns slowly emerging from
certain houses, with goliath size 20 blood stained shoes.
\n
You can:
FIGHT the Clowns
GO NORTH to Traffic Lights
GO SOUTH to Cross Roads""",

	"exits": {"north": "Traffic Lights", "south": "Cross Roads"},

	"items":[],

	"enemies": 3,

	"dead": False,
}

map_talysouth = {
	"name": "Taly South",

	"description": """You arrive safetly back at your flat and
collapse on the once white bed. As you are about to doze off
the sound of the doorbell and knocking pierces your ears, 
as you walk out of your door, the hallway is full to the brim
of fully-armoured police labelled "SWAT", they make their way
to you, standing on the once attatched front door.
The red dots of the guns stain your body, as they handcuff
you hastily, an officer shouts "YOU ARE UNDER ARREST 
FOR THE MASS-MURDER OF MANY INNOCENT PEOPLE ON THE NIGHT OF OCTOBER 31ST
AND FOR DISTRIBUTION AND USE OF CLASS A DRUGS.", 
you fall to the ground in shock as you realise, you are
the monster... END OF GAME""",

	"exits": {},

	"items": [],

	"enemies": 0,

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
