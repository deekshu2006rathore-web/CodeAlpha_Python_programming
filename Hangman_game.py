import random

# Simple list of secret words
WORD_BANK = ["python", "programming", "computer", "keyboard", "science", "software"]

def play_hangman():
    secret_word = random.choice(WORD_BANK).lower()
    guessed_letters = set()
    wrong_attempts = 0
    max_lives = 6

    print("--- WELCOME TO HANGMAN ---")

    while wrong_attempts < max_lives:
        # 1. Display game status (Remaining lives and guessed letters)
        lives_left = max_lives - wrong_attempts
        print(f"\nRemaining Lives: {lives_left}")
        print(f"Letters already guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # 2. Show the word progress (e.g., p _ t h _ n)
        word_display = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print(f"Current Word: {' '.join(word_display)}")

        # 3. Check for win condition
        if "_" not in word_display:
            print(f"\n🎉 Congratulations! You saved the hangman. The word was: '{secret_word.upper()}'")
            break

        # 4. Get and validate user input
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid entry. Please type exactly one single letter.")
            continue
            
        if guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{guess}'. Try a different one.")
            continue

        # 5. Process guess
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            print(f"❌ Wrong! '{guess}' is not in the word.")
            wrong_attempts += 1
            
    else:
        # Triggers only if the loop runs out of lives naturally without a 'break'
        print(f"\n💀 Game Over! You ran out of lives. The correct word was: '{secret_word.upper()}'")

if __name__ == "__main__":
    play_hangman()
