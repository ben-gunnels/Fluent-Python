from dataclasses import dataclass

@dataclass(frozen=True)
class Element:
    name: str
    symbol: str
    number: int
    atomic_mass: float

    def __str__(self):
        """
            Returns an unambiguous human-readable string output.
        """
        width = 10
        output = ""
        output += str(self.number).ljust(int(width / 2)) + str(self.atomic_mass).rjust(int(width/2)) + "\n" # Line 1
        output += self.symbol.center(width) + "\n"
        output += self.name[:10].center(width)
        return output

def main():
    # Row 1
    hydrogen = Element("Hydrogen", "H", 1, 1.0078)
    helium   = Element("Helium", "He", 2, 4.0026)

    # Row 2
    lithium   = Element("Lithium",   "Li", 3, 6.9410)
    beryllium = Element("Beryllium", "Be", 4, 6.9410)
    boron     = Element("Boron",      "B", 5, 10.811)
    carbon    = Element("Carbon",     "C", 6, 12.011)
    nitrogen  = Element("Nitrogen",   "N", 7, 14.007)
    oxygen    = Element("Oxygen",     "O", 8, 15.999)
    fluorine  = Element("Fluorine",   "F", 9, 18.998)
    neon      = Element("Neon",      "Ne", 10,20.180)

    row_1 = [hydrogen, helium]

    row_2 = [lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon]

    print("Row 1 of the Periodic Table: ")
    for element in row_1:
        print("_"*11)
        print(element)
        print("_"*11)
        print("\n")

    print("Row 2 of the Periodic Table: ")
    for element in row_2:
        print("_"*11)
        print(element)
        print("_"*11)
        print("\n")

if __name__ == "__main__":
    main()