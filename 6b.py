# Database of sounds associated with the animals
database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
# Knowledge base containing the animals
knowbase = ["Frog", "Canary"]
# Possible colors for the animals
color = ["Green", "Yellow"]


def display_options():
    """Displays the options for the user to choose an animal."""
    print("\nSelect an animal:")
    print("1. Frog")
    print("2. Canary")
    print("Select one:", end=' ')


def main():
    print("*----- Backward Chaining Algorithm -----*")
    display_options()

    # User input for animal selection
    animal_choice = int(input())
    print("\n", end='')

    if animal_choice == 1:
        print("Chance of eating flies", end='')
    elif animal_choice == 2:
        print("Chance of shrimping", end='')
    else:
        print("\n------- Invalid Option Selected -------", end='')
        return  # Exit if the selection is invalid

    if animal_choice in [1, 2]:
        print("\nSelected Animal: ", end='')
        print(knowbase[animal_choice - 1], end='')  # Display selected animal
        print("\nAvailable Colors:")
        print("1. Green")
        print("2. Yellow")

        # User input for color selection
        color_choice = int(input())

        # Determine the sound based on the animal and color selected
        if color_choice == 1 and animal_choice == 1:  # Frog and Green
            print("Yes, it is a ", end='')
            print(color[0], end='')  # Green
            print(" color and will ", end='')
            print(database[0])  # Croaks
        elif color_choice == 2 and animal_choice == 2:  # Canary and Yellow
            print("Yes, it is a ", end='')
            print(color[1], end='')  # Yellow
            print(" color and will ", end='')
            print(database[1])  # Eat Flies
        else:
            print("\n--- Invalid Knowledge Database ---", end='')


if __name__ == "__main__":
    main()
