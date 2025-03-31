def get_product(record: dict) -> list:
    match record:
        case { "product": "eggs", "count": count, "desc": [*desc] }:
            return ["eggs", count] + desc
        
        case { "product": "milk", "volume": volume, "desc": [*desc]}:
            return ["milk", volume] + desc
        
        case { "product": "milk", "volume": volume, "desc": desc}:
            return ["milk", volume, desc]
        
        case { "product": "onion", "weight": weight, "desc": desc}:
            return ["onion", weight, desc]
        case _:
            raise ValueError(f'Invalid Record: {record!r}')

product_inventory = [
    { "product": "eggs", "count": 12, "desc": ["Farm-Fresh", "Pasteurized", "AA", "White"] },
    { "product": "eggs", "count": 18, "desc": ["Farm-Fresh", "Pasteurized", "AAA", "No-Antibiotics"] },
    { "product": "milk", "volume": "1 gal", "desc": ["Pasteurized", "Whole"]},
    { "product": "milk", "volume": "1/2 gal", "desc": "2%"},
    { "product": "onion", "weight": "8 oz", "desc": "Yellow"},
    { "product": "onion", "weight": "13 oz", "desc": "Red"},
    { "product": "Potato", "weight": "16 oz", "desc": "Red"},
]

# Which products will be parsed correctly? How can we manage this so unexpected data is handled more gracefully?
for product in product_inventory:
    product_summary = get_product(product)
    print(product_summary)