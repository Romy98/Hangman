import random

words = ['computer', 'python', 'entrepreneur', 'one', 'piece']
correct_letters = ['']
wrong_letters = ['']
correct_answers = 0
is_over = False

def word_to_guess(words):
    word = random.choice(words)
    return word

def choose_letter():
    tries = 6
    word = list(word_to_guess(words))
    masked = []
    for letter in word:
        masked.append('-')
    print(f'This is the word you need to guess: {masked}\nIt has {len(masked)} letters')
    while (tries > 0):
        count = 0
        letter = input('Enter a letter: ')
        for x in word:
            if letter in word:
                masked[word.index(letter)] = letter
                correct_letters.append('letter')
                print(masked)
                count += 1
                break
            elif letter not in word:
                print('Wrong pick! Try again.')
                wrong_letters.append('letter')
                if tries == 1:
                    print("Game Over!")
                count += 1
                tries -= 1
                break


choose_letter()