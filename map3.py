#from items import *

map_pryzym {
	"name": "Pryzm",

	"description": """You stumble out of Pryzym as it 
	closes, and find yourself on a dark street 
	surrounded by people near a taxi rank. You prepare
	 yourself for the long walk home, wishing 
	Pryzym had stayed open just a little bit longer.
	Do you want to walk EAST to the Student Union or 
	go WEST through the Park? """,

	"exits": {"east" : "Student Union", "west" : "Park"},

	"items": [item_bottle],

	"enemies": 0
}
map_park{
	"name": "Park",

	"description": """You walk through the park it is
	 surprisingly quiet, there is litter on the
	ground you pick up a needle amongst the debry.
	There are lights on in the Museum. You see a clown
	opposite you, you run. 
	Do you want to run WEST or EAST?""",

	"exits": {"west": "Museum", "east": "Museum"},

	"items": [item_needle],

	"enemies": 0
}
map_museum{
	"name": "Museum",

	"description": """You run into the Museum, you can hear
	distant music, you are safe from the clown. You stand in
	the lobby area and look around... A statue comes to life
	and stabs you with your needle in your heart... YOU DIE!""",

	"exits": {},

	"items": [item_needle],

	"enemies": 0

}

map_lidl{
	"name": "Lidl",

	"description": """You walk down the lit road towards Lidl,
	you see a shotgun lying in the car park, you run towards 
	it and just as you pick it up, a clown stabs you in the back.
	YOU DIED...""",

	"exits": {},

	"items": [item_shotgun],

	"enemies": 20
}

map_su{
	"name": "Student Union",

	"description": """The lights flicker as you enter the SU, 
	you see a cricket bat lying amongst the dead bodies 
	of the cricket society. A clown is standing in front of you 
	covered in blood. 
	Do you want to fight or run?""",

	"description2": """To EAST is Lidl and to the WEST is the 
	Cross Roads. 
	Where do you want to go?"""

	"exits": {"east": "LIDL", "west": "Cross Roads"},

	"items": [item_cricket_bat],

	"enemies": 1,
}

map_crossroads{
	"name": "Cross Roads",

	"description": """You are at the cross roads, everything
	look safe, there is a Letting Office, a coffee shop and
	the Law and Politics Building. You can go EAST for Lidl
	or NORTH towards the Traffic Lights.
	Which way do you want to walk home?  """,

	"exits": {"east": "Lidl", "west": "Coffee Shop", "north": "Traffic Lights"},

	"items": [item_bottle:3],

	"enemies": 0,
}

map_coffee{
	"name": "Coffee Shop",

	"description": """You break the glass of the coffee shop
	and walk in. 
	Do you want to loot some coffee?""",

	"exits": {"south": "Cross Roads"},

	"items": [item_coffee],

	"enemies":0,

} 

map_traffic{
	"name": "Traffic Lights",

	"description": """You come to the Traffic Lights and wait
	for them turn red for you to cross, a car with a red nose
	on the grill stops. You start to cross as 10 clowns pour
	out of the clown car. 
	What do you want to do RUN or FIGHT?""",

	"exits": {"south": "Cross Roads", "North": "Taly South"},

	"items": [],

	"enemies":10
}

map_emptyrd{
	"name": "Empty Road",

	"description": """There are bins littered all up the street,
	you can hear the music coming from the student houses. You 
	try to get in but cannot. There are clowns lining the streets.
	Do you want to run NORTH towards Taly South or fight?""",

	"exits": {"north": "Traffic Lights", "south": "Cross Roads"},

	"items":[],

	"enemies": 3
}

map_talysouth{
	"name": "Taly South",

	"description": """You arrive safetly back at your flat and 
	fall asleep. You wake up to the sound of knocking on your door, 
	when you open it a police officer puts cuffs on you.
	"you're under arrest for the suspicion of the mass 
	killings that took place on halloween night". Well done, 
	you're a drug addict, you'd been hallucinating :D"""

	"exits": {},

	"items": [],

	"enemies": 0 
}

places = {
	"Pryzm": map_pryzm
	"Lidl": map_lidl
	"Student Union": map_su
	"Cross Roads": map_crossroads
	"Taly South": map_talysouth
	"Empty Road": map_emptyrd
	"Coffee Shop": map_coffee
	"Traffic Lights": map_traffic
	"Park": map_park
	"Museum": map_museum
}