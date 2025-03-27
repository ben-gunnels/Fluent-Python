

def main():
    # Make every element an X
    good_etch_a_sketch = [["X"] * 10 for _ in range(10)]
    weird_etch_a_sketch = [["X"] * 10] * 10
    
    # Try to make the 3rd element of the second row an O
    good_etch_a_sketch[1][2] = "O"
    weird_etch_a_sketch[1][2] = "O"

    # Compare the checkerboards. How are they different? What did you expect to happen?
    print("Good Etch a Sketch")
    for row in good_etch_a_sketch:
        print(row)
    print("\n")

    print("Weird Etch a Sketch")
    for row in weird_etch_a_sketch:
        print(row)
    print("\n")

    # Reset sketch pads
    good_etch_a_sketch[1][2] = "X"
    weird_etch_a_sketch[1][2] = "X"

    # Make the diagonal fill with Os
    for row in range(len(good_etch_a_sketch)):
        for col in range(len(good_etch_a_sketch[row])):
            if row == col:
                good_etch_a_sketch[row][col] = "O"
                weird_etch_a_sketch[row][col] = "O"

    # Compare the checkerboards. How are they different? What did you expect to happen?
    print("Good Etch a Sketch")
    for row in good_etch_a_sketch:
        print(row)
    print("\n")

    print("Weird Etch a Sketch")
    for row in weird_etch_a_sketch:
        print(row)
    print("Oops its all Os")
    print("\n")


if __name__ == "__main__":
    main()