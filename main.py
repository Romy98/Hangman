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

def masked_word(word):
    word = list(word_to_guess(words))
    masked = []
    print(word)
    for letter in word:
        masked.append('-')
    print(masked)