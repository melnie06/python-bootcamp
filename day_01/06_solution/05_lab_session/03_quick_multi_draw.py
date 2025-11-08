from random import choice

options = ["rock", "paper", "scissors"]


def get_user_choice():
    while True:
        user_choice = input("Pick a choice (rock/paper/scissors): ").lower()
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

def play_round():
    player_choice = get_user_choice()
    cpu_choice = get_cpu_choice()
    result = get_winner(player_choice, cpu_choice)

    print(f"Player chose {player_choice}, CPU chose {cpu_choice}")
    if result == "Draw":
        print("It's a draw!")
    else:
        print(result, "won the round!")
    return result

def game():
    total_rounds = int(input("Best of how many rounds? (odd number only): "))
    while total_rounds % 2 == 0:
        total_rounds = int(input("Please enter an odd number: "))

    player_score = 0
    cpu_score = 0
    rounds_to_win = total_rounds // 2 + 1

    while player_score < rounds_to_win and cpu_score < rounds_to_win:
        result = play_round()
        if result == "Player":
            player_score += 1
        elif result == "CPU":
            cpu_score += 1
        print(f"Score: Player {player_score} - CPU {cpu_score}\n")

    print("Game Over!")
    if player_score > cpu_score:
        print("Player wins the game!")
    else:
        print("CPU wins the game!")


game()
