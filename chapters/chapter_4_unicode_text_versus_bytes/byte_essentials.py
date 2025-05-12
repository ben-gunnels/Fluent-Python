import sys

def main():
    # build a bytes object from a string
    marmalade = bytes('marmalade', encoding='utf_8')
    print(marmalade)
    print(f"Marmalade Bytes Size: {sys.getsizeof(marmalade)}")

    # Each item is an 8 bit integer
    print(marmalade[0])
    print(f"Marmalade Bytes[0] Size: {sys.getsizeof(marmalade[0])}")

    # Slices of bytes are bytes
    print(marmalade[:1])
    print(f"Marmalade Bytes[:1] Size: {sys.getsizeof(marmalade[:1])}")

    marmalade_arr = bytearray(marmalade)
    print(marmalade_arr)
    print(f"Marmalade Array Size: {sys.getsizeof(marmalade_arr)}")

    # A slice of the bytes array
    print(marmalade_arr[-1:])
    print(f"Marmalade Array Slice Size: {sys.getsizeof(marmalade_arr[-1:])}")

    # Print the size of a string for reference
    marmalade_str = "marmalade"
    print(f"Marmalade String Size: {sys.getsizeof(marmalade_str)}")

if __name__ == "__main__":
    main()