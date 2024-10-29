# Import necessary libraries
from random import randint

# Define file path for top players
file_path = r"D:\PhD_UMMC\Python_1\Assignment 10\topPlayers.txt"

def display_top_players():
    """Display the top players from the file."""
    try:
        with open(file_path, "r") as file:
            players = file.readlines()
            print("\nTop Players:")
            for player in players:
                print(player.strip())
    except FileNotFoundError:
        print("Top players file not found.")

def update_top_players(name, score):
    """Update the top players file with the new score and return the updated list."""
    players = []
    try:
        # Read existing players from the file
        with open(file_path, "r") as file:
            players = [line.strip().split(maxsplit=1) for line in file.readlines()]

        # Add new player
        players.append([str(score), name])
        players.sort(key=lambda x: int(x[0]))  # Sort by score (ascending)

        # Keep only the top 5 players
        players = players[:5]

        # Save the updated list back to the file
        with open(file_path, "w") as file:
            for player in players:
                file.write(f"{player[0]:<10}{player[1]}\n")

    except FileNotFoundError:
        print("Top players file not found. Creating a new one.")
        players.append([str(score), name])  # Create a new list if the file doesn't exist
        with open(file_path, "w") as file:
            file.write(f"{score:<10}{name}\n")

    return players  # Return the updated list

# Main loop for multiple players
while True:
    # Ask for player's name
    player_name = input("Enter your name: ")

    # Check if the player wants to stop
    if player_name == "STOP":
        print("Game finished. No More Players to Play!")
        break  # Exit the loop to stop the game
    # Start the game
    some_number = randint(1, 100)
    number_of_guesses = 0
    correct_guess = 0

    print(f"\nWinning Number: {some_number}")

    while correct_guess == 0:
        try:
            player_guess = input("What is your guess? ")

            # Check if the player wants to quit
            if player_guess == 'q':
                print("Thanks for playing!")
                break

            # Validate the guess
            if player_guess.isnumeric():
                number_of_guesses += 1
                player_guess = int(player_guess)

                # Test for a low guess
                if player_guess < some_number:
                    print(f"{player_guess} is too low. Guess again.")

                # Test for a high guess
                elif player_guess > some_number:
                    print(f"{player_guess} is too high. Guess again.")

                # Correct guess
                else:
                    print(f"{player_guess} IS CORRECT!")
                    print(f"It took {player_name} {number_of_guesses} guesses.")
                    top_players = update_top_players(player_name, number_of_guesses)
                    correct_guess = 1

            else:
                print(f"Please choose an integer between 1 and 100.")

        except EOFError:
            print(f"Looks like you wanted to get out of the game early!")
            correct_guess = 1

        except Exception as e:
            print(f"Well... some type of error occurred.\nThank you for playing!")
            correct_guess = 1

    # Display updated top players
    print("\nTop Players:")
    for score, name in top_players:  # Directly use the updated players
        print(f"{score:<10}{name}")

    # Ask to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == 'n':
        print("Thank you for playing!")
        # After thanking the player, prompt for a new player's name
        continue  # Skip to the next iteration for a new player
    elif play_again != 'y':
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

print(f"Game finished. See you in tomorrow's game")
