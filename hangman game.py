import random

# Predefined list of words
words = ["apple", "house", "plant", "train", "chair"]

# Randomly select a word
word = random.choice(words)
word_letters = list(word)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word_letters:
        tries -= 1
        print("Wrong guess! Tries left:", tries)
    else:
        print("Correct guess!")

    display_word = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    if all(letter in guessed_letters for letter in word_letters):
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("Game Over! The word was:", word)