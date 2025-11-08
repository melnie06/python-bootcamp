from random import choice

options = ("rock", "paper", "scissors")

def get_user_choice():
    while True:
        user_choice = input("Pick a choice (rock/paper/scissors): ")
        if user_choice in options:
            return user_choice

def get_cpu_choice():
    return choice(options)

def get_winner(player, cpu):
    if player == cpu:
        return "Draw"
    elif (
            (player == "rock" and cpu == "scissors") or
            (player == "paper" and cpu == "rock") or
            (player == "scissors" and cpu == "paper")
    ):
        return "Player"
    else:
        return "CPU"

def game():
    player_choice = get_user_choice()
    cpu_choice = get_cpu_choice()
    result = get_winner(player_choice, cpu_choice)

    print(f"Player chose {player_choice}, CPU chose {cpu_choice}")
    if result == "Draw":
        print("It's a draw!")
    else:
        print(result, "won!")

game()
