retail_data = """
0.....6.................................40...........52...55........
1717  QuantumBlend Coffee                       $8.50   14   $119.00
7002  NeonFlex Headphones                      $67.99    4   $271.96
2314  AeroShield Phone Case                    $14.75   12   $177.00
1212  HydroGlow Water Bottle                    $9.99   41   $409.59"""

def main():
    SKU = slice(0, 6)
    ITEM_DESC = slice(6, 40)
    ITEM_PRICE = slice(40, 52)
    ITEM_QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)

    line_items = retail_data.split("\n")[2:] # Skip the prefixed dots

    for item in line_items:
        print(f"{item[ITEM_PRICE]}: {item[ITEM_DESC]}")

if __name__ == "__main__":
    main()      