def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('_________________')
        print(key)
        for i in options[question_num - 1]:
            print(i)

        guess = input("Enter (A, B, C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_ans(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_ans(answer, guess):
    if answer == guess:
        print("✅ Correct!")
        return 1
    else:
        print("❌ Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("_________________")
    print("       RESULTS")
    print("-----------------")
    
    print("Correct Answers: ", end=" ")
    for key in questions:
        print(questions.get(key), end=" ")
    print()

    print("Your Guesses:    ", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print(f"\nYour Score: {score}% 🎯")


def play_again():
    response = input("\nDo you want to play again? (yes/no): ").lower()
    if response == "yes":
        new_game()
    else:
        print("Thanks for playing! 🧠")


questions = {
    "Who created Python?": "A",
    "What year RCB won?": "C",
    "When is your birthday?": "B",
}

options = [
    ['A: Guido van Rossum', 'B: Elon Musk', 'C: Narendra Modi', 'D: Iron Man'],
    ['A: Dukhti nas pe haath', 'B: Har baar', 'C: Kabhi nahi', 'D: 2016'],
    ['A: Kal tha', 'B: Kal hai', 'C: Ho gaya bhai', 'D: Kya yaad dilaya'],
]

# Start game
new_game()
play_again()
