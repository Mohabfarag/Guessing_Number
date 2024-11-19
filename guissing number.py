import random

def welcome():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 100.")
    print("Your goal is to guess the number in as few attempts as possible.")
    print("Let's get started!\n")

def get_random_number():
    return random.randint(1, 100)  # Generates a random number between 1 and 100

def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def check_guess(guess, correct_number):
    if guess < correct_number:
        print("Too low! Try again.")
        return False
    elif guess > correct_number:
        print("Too high! Try again.")
        return False
    else:
        print(f"Congratulations! You've guessed the number {correct_number} correctly!")
        return True

def main():
    welcome()
    correct_number = get_random_number()
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = get_player_guess()
        attempts += 1
        guessed_correctly = check_guess(guess, correct_number)

    print(f"It took you {attempts} attempts to guess the correct number.")

if __name__ == "__main__":
    main()
