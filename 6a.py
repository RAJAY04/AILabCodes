# Knowledge and database setup
database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary", "Green", "Yellow"]

# Display options for user selection
def display():
    print("\nChoose an observation about the animal:")
    print("1. Croaks")
    print("2. Eat Flies")
    print("3. Shrimps")
    print("4. Sings")
    print("Select one: ", end='')

# Main function implementing forward chaining
def main():
    print("---- Forward Chaining ----")
    display()
    x = int(input())
    print("")

    if x == 1 or x == 2:
        print("Chance of it being a Frog.")
    elif x == 3 or x == 4:
        print("Chance of it being a Canary.")
    else:
        print("Invalid Option Selected")
        return

    if 1 <= x <= 4:
        print(f"\nObservation: {database[x-1]}")
        print("Choose the color:")
        print("1. Green")
        print("2. Yellow")
        print("Select one: ", end='')
        k = int(input())

        if k == 1 and (x == 1 or x == 2):  # Frog and green
            print(f"Yes, it is a {knowbase[0]} and it is {knowbase[2]} in color.")
        elif k == 2 and (x == 3 or x == 4):  # Canary and yellow
            print(f"Yes, it is a {knowbase[1]} and it is {knowbase[3]} in color.")
        else:
            print("Invalid Knowledge Database")


main()
