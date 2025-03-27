"""
(common name, color, type, (scientific name, family, class, genus, kingdom, order))
"""

tree_data = [ 
    ("elm", "green", "deciduous", ("ulmus", "ulmaceae", "magnoliopsida", "ulmus l", "plantae", "rosales")),
    ("fir", "green", "coniferous", ("abies", "pinaceae", "pinopsida", "abies", "plantae", "pinales")),
    ("juniper", "green", "coniferous", ("juniperus", "cupressaceae", "pinopsida", "juniperus", "plantae", "cupressales")),
    ("oak", "green", "deciduous/evergreen", ("quercus", "fagaceae", "dicotyledon", "quercus l", "plantae", "fagales")),
    ("norway spruce", "green", "coniferous", ("picea abies", "pinaceae", "pinopsida", "picea", "plantae", "pinales")),
]



def main():
    # match the records to pinaceae family
    for record in tree_data:
        match record:
            case [name, color, typ, (sn, f, c, g, k, o)] if f == "pinaceae":
                print(f"{name}:")
                print(f"species: {sn}")
                print(f"family: {f}")
                print(f"class: {c}")
                print(f"order: {o}")
                print("\n")


    # Count the families
    family_counts = {}

    for (name, color, typ, (sn, f, c, g, k, o)) in tree_data:
        family_counts[f] = family_counts.get(f, 0) + 1

    print(family_counts)
    print("\n")

    type_counts = {}
    for (_, _,  typ, *_) in tree_data: # Just get the value of interest
        type_counts[typ] = type_counts.get(typ, 0) + 1
    
    print(type_counts)


if __name__ == "__main__":
    main()