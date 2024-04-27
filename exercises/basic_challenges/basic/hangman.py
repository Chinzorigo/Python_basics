import random


def hangman():
    words = ["python", "hangman", "game", "programming", "fun"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 7

    print("Welcome to Hangman!")

    while attempts > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "-"

        print(guessed_word)

        if guessed_word == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1

        print("Attempts left:", attempts)

    else:
        print("Sorry, you ran out of attempts. The word was:", word)


hangman()
