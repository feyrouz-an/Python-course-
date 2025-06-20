import random
player_wins = 0
computer_wins = 0

for rounds in range(3):
    print("Options are: Rock, Paper, Scissors")
    p1 = input("Player 1, enter your choice: ").strip().lower()
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer}")

    if p1 == computer:
        print("It's a tie!")
    elif (
        (p1 == "rock" and computer == "scissors") or
        (p1 == "paper" and computer == "rock") or
        (p1 == "scissors" and computer == "paper")
    ):
        print("Player 1 wins this round!")
        player_wins += 1
    elif (
        (computer == "rock" and p1 == "scissors") or
        (computer == "paper" and p1 == "rock") or
        (computer == "scissors" and p1 == "paper")
    ):
        print("Computer wins this round!")
        computer_wins += 1
    else:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")

if player_wins > computer_wins:
    print("Player 1 is the final winner!")
elif computer_wins > player_wins:
    print("Computer is the final winner!")
else:
    print("It's a tie overall!")