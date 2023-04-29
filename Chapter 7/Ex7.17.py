# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0},  winner={1} ".format(human_plays_first, result))
    return result


def game():
    player_wins = 0
    computer_wins = 0
    number_of_ties = 0

    while True:
        who_wins = play_once(True)
        if who_wins == 1:
            computer_wins += 1
            print("I win!")
        elif who_wins == -1:
            player_wins += 1
            print("You win!")
        elif who_wins == 0:
            number_of_ties += 1
            print("Game drawn!")
        print("You have", player_wins, "wins and the computer has", computer_wins, "wins. There are",
              number_of_ties, "draws.")
        total_games = number_of_ties + player_wins + computer_wins
        win_rate = player_wins / total_games * 100
        print("Your win rate is", win_rate, "%")
        response = input("Do you want to play again? ")
        if response == "no" or response == "No":
            print("Goodbye")
            return False


game()
