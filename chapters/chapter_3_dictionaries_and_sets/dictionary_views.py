user_table = {
    "georgie012":       {"id": 10023001, "groups": ["farming", "cooking", "skiing"]},
    "pandabearx0":      {"id": 10023002, "groups": ["crafts", "wine", "skiing"]},
    "dragonfire512":    {"id": 10023003, "groups": ["gaming", "art"]},
    "rumpelstiltskin":  {"id": 10023004, "groups": ["riddles", "music"]},
    "jeremy651":        {"id": 10023005, "groups": ["football", "hunting", "snowboarding"]},
    "rebekkah_s":       {"id": 10023006, "groups": ["legos", "crafts"]},
    "timmy_tom":        {"id": 10023007, "groups": ["cooking", "dance", "comedy"]},
    "rangoranger":      {"id": 10023008, "groups": ["reading", "wine", "technology"]},
    "hollyb":           {"id": 10023009, "groups": ["travel", "hiking", "music"]},
}

view = user_table.keys()
print(f"View ID: {id(view)}")
print(f"View before update: {view}")

new_user = "luciano"
new_user_data = {"id": 10023010, "groups": ["programming", "travel", "writing"]}

user_table[new_user]  = new_user_data

# Notice how the view is updated automatically when the original dict has been updated. 
print(f"View ID: {id(view)}")
print(f"View after update: {view}")