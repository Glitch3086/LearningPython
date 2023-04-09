import random

def get_choices():
    player_choice = input("Enter a Choice (Rock, Paper, Scissor: )")
    possible_choice = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(possible_choice)
    choises = {"player": player_choice, "computer": computer_choice}
    return choises

def check_win(player, computer):
    print(f"You choose: {player}, computer choose: {computer}")
    # checks to see if there is a tie
    if player == computer: 
        return "It's a Tie"

    # Checks for win if palyer chose rock
    elif player == "Rock":
        if computer == "Scissor":
            return "Rock smaches Scissor. You Win!"
        else:
            return "Paper covers Rock. You Lose!"

    # Checks for win if palyer chose Paper
    elif player == "Paper":
        if computer == "Scissor":
            return "Scissor cuts Paper. You Lose!"
        else:
            return "Paper covers Rock. You Win!"
            
    # Checks for win if palyer chose Scissor
    elif player == "Scissor":
        if computer == "Rock":
            return "Rock smaches Scissor. You Win"
        else:
            return "Scissor cuts Paper. You Lose!"

check_win("Rock", "Paper")