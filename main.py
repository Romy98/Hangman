import random

words = ['computer', 'python', 'entrepreneur', 'One', 'Piece']
correct_letters = ['']
wrong_letters = ['']
correct_answers = 0
tries = 6
is_over = False

def word_to_guess(words):
    word = random.choice(words)
    return word

def choose_letter():
    word = list(word_to_guess(words))
    masked = []
    for letter in word:
        masked.append('-')
    print(f'This is the word you need to guess: {masked}\nIt has {len(masked)} letters')
    letter = input('Enter a letter: ')

choose_letter()