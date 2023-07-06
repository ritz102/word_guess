import random

options_list = ["apple", "chair", "hello", "world", "music"]  # Add your own list of words here

def input_word():
    while True:
        guess = input("Enter a 5-letter word: ")
        if len(guess) != 5:
            print("Enter a 5-letter word, Your guess has", len(guess), "letters.")
        elif not guess.isalpha():
            print("Wrong guess...try again")
        else:
            return guess

def alphamark(guess, rightanswer):
    return [letter if letter == guess[idx] else '_' for idx, letter in enumerate(rightanswer)]

def game_play():
    attempts = 0
    rightanswer = random.choice(options_list)

    while attempts < 5:
        attempt = input_word()
        marked_letters = alphamark(attempt, rightanswer)
        print(' '.join(marked_letters))

        if attempt == rightanswer:
            print("Your guess is correct!")
            return

        attempts += 1

    print("Your attempts are finished....The answer is:", rightanswer)
    print('Bye ! ')
def adding_word():
    neword_add = input("Would you like to add a word? ")
    if neword_add.lower() in ["y", "yes"]:
        what_word = input("Enter a 5-letter word of your choice: ")
        if len(what_word) != 5:
            print("Enter a 5-letter word. Your current word has", len(what_word), "letters.")
            adding_word()
        elif what_word in options_list:
            print("Your input already exists, try again !")
            adding_word()

        else:
            options_list.append(what_word)
            print("The word", what_word, "has been added to the list of words!")
    game_play()
adding_word()
