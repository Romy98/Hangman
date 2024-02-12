import random

words = ['computer', 'python', 'entrepreneur', 'One', 'Piece']
correct_letters = ['']
wrong_letters = ['']
correct_answers = 0
tries = 6
is_over = False

def word_to_guess(words):
    word = random.choice(words)
    print(word)

word_to_guess(words)

