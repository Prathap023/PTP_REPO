import random

def select_random_word():
    words = ['python', 'hangman', 'programming', 'openai', 'developer']
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display_word

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_current_progress(word, guessed_letters)}")
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        print(f"Incorrect Guesses Left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
            
            if set(word) == guessed_letters:
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print("Incorrect guess.")
    
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

# Run the game
hangman()