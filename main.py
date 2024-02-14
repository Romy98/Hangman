
import random

def choose_word():
    words = ["hangman", "python", "programming", "developer", "coding", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    lives = max_attempts
    guessed_letters = []
    word_to_guess = choose_word()

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
    print(f"You have {lives} lives.")

    while lives > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")
        else:
            print("Good guess!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print(f"Congratulations! You guessed the word '{word_to_guess}'.")
            break

    if "_" in current_display:
        print(f"Sorry, you ran out of lives. The word was '{word_to_guess}'.")



if __name__ == "__main__":
    hangman()