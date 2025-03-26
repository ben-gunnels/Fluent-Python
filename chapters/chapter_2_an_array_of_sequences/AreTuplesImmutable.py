def fixed(o):
    """
        Checks if an object is hashable i.e. is it immutable?
        If an object is immutable it can be used as a key
    
    """
    try:
        hash(o)
    except TypeError:
        return False
    return True


def main():
    # Hashable tuple
    car_1 = ('toyota', 'camry', 'red', 2024, (28, 39)) # Make, Model, Color, Year, (Gas Mileage City, Gas Mileage Highway)
    # Unhashable tuple
    car_2 = ('mazda', 'cx-5', 'white', 2024, [26, 31]) # Make, Model, Color, Year, [Gas Mileage City, Gas Mileage Highway]

    lot_inventory = {}

    for car in [car_1, car_2]:
        print(f"{car} hashable: {fixed(car)}")
        try:
            lot_inventory[car] = 10
        
        except TypeError:
            print("Car data is not hashable")
    
    print(lot_inventory)


if __name__ == "__main__":
    main()