import random

def hangman():
    words = ["python", "programming", "hangman", "challenge"]
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
   
    while attempts > 0 and ''.join(guessed_word) != word:
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = letter
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word.")

    if ''.join(guessed_word) == word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game Over! The word was: {word}")

hangman()
