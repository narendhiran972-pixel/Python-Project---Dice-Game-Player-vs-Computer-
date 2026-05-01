import random
import time

print("🎲 Welcome to Dice Game (Player vs Computer)")

player_score = 0
computer_score = 0
round_no = 1

while True:
    print("\n-----------------------------")
    print("Round:", round_no)

    input("Press Enter to roll the dice...")

    print("Rolling dice...")
    time.sleep(1)

    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    print("You rolled:", player)
    print("Computer rolled:", computer)

    if player > computer:
        print("🎉 You Win this round!")
        player_score += 1
    elif player < computer:
        print("💻 Computer Wins this round!")
        computer_score += 1
    else:
        print("🤝 It's a Draw!")

    print("\nScore Board")
    print("You:", player_score)
    print("Computer:", computer_score)

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("\nFinal Score")
        print("You:", player_score)
        print("Computer:", computer_score)

        if player_score > computer_score:
            print("🏆 Overall Winner: You!")
        elif player_score < computer_score:
            print("🏆 Overall Winner: Computer!")
        else:
            print("🤝 Match Draw!")

        print("Thanks for playing!")
        break

    round_no += 1