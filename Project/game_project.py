import random

def Game():
    while True:
        choices = ["rock", "paper", "scissor"]
        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("rock, paper, or scissor? ").lower()

        if player == computer:
            print("Computer:", computer)
            print("Player:", player)
            print("Tie!")
        elif player == "paper":
            if computer == "scissor":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
            elif computer == "rock":
                print("Computer:", computer)
                print("Player:", player)
                print("You WIN!!")
        elif player == "scissor":
            if computer == "rock":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
            elif computer == "paper":
                print("Computer:", computer)
                print("Player:", player)
                print("You WIN!!")
        elif player == "rock":
            if computer == "paper":
                print("Computer:", computer)
                print("Player:", player)
                print("You lose!")
            elif computer == "scissor":
                print("Computer:", computer)
                print("Player:", player)
                print("You WIN!!")

        a = input("Do you want to play again, say y/n: ").lower()
        if a != "y" and a != "yes":
            print("Thank you and have a nice day!")
            break

Game()
