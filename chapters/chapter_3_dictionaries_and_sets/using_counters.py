import collections

user_table = {
    "georgie012":       {"id": 10023001, "groups": ["farming", "cooking", "skiing"]},
    "pandabearx0":      {"id": 10023002, "groups": ["crafts", "wine", "skiing", "diy"]},
    "dragonfire512":    {"id": 10023003, "groups": ["gaming", "art", "new music", "movies"]},
    "rumpelstiltskin":  {"id": 10023004, "groups": ["riddles", "music", "climbing"]},
    "jeremy651":        {"id": 10023005, "groups": ["football", "hunting", "snowboarding", "book club"]},
    "rebekkah_s":       {"id": 10023006, "groups": ["legos", "crafts", "technology", "exploring"]},
    "timmy_tom":        {"id": 10023007, "groups": ["cooking", "dance", "comedy"]},
    "rangoranger":      {"id": 10023008, "groups": ["reading", "wine", "technology"]},
    "hollyb":           {"id": 10023009, "groups": ["travel", "hiking", "music", "art"]},
}


user_groups = []

for key, val in user_table.items():
    for group in val["groups"]:
        user_groups.append(group)


class CustomCounter(collections.Counter):
    def __repr__(self):
        _repr = "CustomCounter(\n"
        for key, value in sorted(self.items(), key=lambda x: x[1], reverse=True):
            _repr += f"{key}: {value}\n"
        _repr += ")"
        return _repr

user_groups_count = CustomCounter(user_groups)

print(user_groups_count)