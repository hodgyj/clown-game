import items
# map.py
map_pryzm{}

map_park{}

map_museum{}

map_su{"name": "Student Union",
"description": """

""",
"items": [cricket_bat],
"enemies": 1
}

map_lidl{"name": "Lidl",
"description":"""

""",
"items": [shotgun],
"enemies": 20
}

map_crossroads{}

map_coffee{}

map_traffic{}

map_emptyrd{}

map_talysouth{"name": "Taly South",
"description":"""

""",
"items": [],
"enemies": 1}

places = {
    "pryzm": map_pryzm,
    "park": map_park,
    "museum": map_museum,
    "su": map_su,
    "lidl": map_lidl,
    "cross roads": map_crossroads,
    "coffee": map_coffee,
    "traffic lights": map_traffic,
    "empty road": map_emptyrd,
    "taly south": map_talysouth
}
