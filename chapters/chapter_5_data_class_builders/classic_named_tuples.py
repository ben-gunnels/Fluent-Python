from collections import namedtuple

ProductionInfo = namedtuple("ProductionInfo", "manufacturer model patent_no")
Product = namedtuple("Product", 'name sku price inventory production_info')

def main():
    # Define some products
    toaster       = Product("Toaster",       "1001820EX", 19.99, 3_000, ProductionInfo("Metal Corp",       "HB1079",          1001040551))
    air_fryer     = Product("Air Fryer",     "1290012AC", 49.99, 1_000, ProductionInfo("Samurai Cook Co.", "Whirlpool 7",     1020010440))
    bottle_opener = Product("Bottle Opener", "1442988YK", 9.99,  10_000, ProductionInfo("Popware",         "Celebration 2.0", 1110010340))

    # Output some of the attributes
    print(f"Product: {toaster.name}, SKU: {toaster.sku}, Price: {toaster.price}, In Stock: {toaster.inventory}, Company: {toaster.production_info.manufacturer}")
    print("\n")
    print(f"Product: {bottle_opener.name}, SKU: {bottle_opener.sku}, Price: {bottle_opener.price}, In Stock: {bottle_opener.inventory}, Company: {toaster.production_info.manufacturer}")
    print("\n")
 
    # Demonstrate some attributes and methods
    print(f"Air Fryer Attributes: {air_fryer._fields}")
    print("\n")

    # Create a new product using the ._make method
    rubber_spatula_data = ("Rubber Spatula", "1991079BT", 8.99, 10_000, ProductionInfo("Serenity Home Goods", "Warm Sunset", 1030010040))
    print("\n")
    rubber_spatula = Product._make(rubber_spatula_data)

    # Print the product as a dictionary
    print(rubber_spatula._asdict())

if __name__ == "__main__":
    main()