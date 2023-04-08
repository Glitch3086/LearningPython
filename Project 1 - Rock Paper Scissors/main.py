import random

def get_choices():
    player_choice = input("Enter a Choice (Rock, Paper, Scissor: )")
    possible_choice = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(possible_choice)
    choises = {"player": player_choice, "computer": computer_choice}
    

    return choises

choises = get_choices()
print(choises)