import random


# define roll function
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# Get total number of players
while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players")
    else:
        print("Invalid input, please enter a number between (2-4)")

# Set max score and build score table
max_score = 50
player_scores = [0 for _ in range(players)]

# Begin game loop until a player hits over max score
while max(player_scores) < max_score:

    # Loop through each player turn
    for player_index in range(players):
        print("\nPlayer", player_index + 1, "turn has started.\n")
        print("Your total score is currently", player_scores[player_index])
        current_score = 0

        # Start players turn
        while True:

            # Check if player wants to roll
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()

            # Break out of players turn if the roll a 1
            if value == 1:
                print("You rolled a 1! Turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your current score is:", current_score)

        # Update players score with turn score
        player_scores[player_index] += current_score
        print("Your total score is: ", player_scores[player_index])

# Handle winning player and end game
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number", winning_index + 1,
      "is the winner with a score of:", max_score)
