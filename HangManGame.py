from numpy import random
words = ["nayan", "apple", "train", "chair", "water"]
secret_word = random.choice(words) # pick a random word from the words as a secret word
guessed_words = []
attempts_left = 6
# print(secret_word)
print("Welcome to the HangMan Game...!")
print("_" * len(secret_word)) # intial display
while attempts_left > 0:
    guess = input("Enter the character: ").lower()
    # check if already guessed
    if guess in guessed_words:
        print("You already guessed the word")
        continue
    guessed_words.append(guess)
    # check if guess word is correctly guessed
    if guess in secret_word:
        print("Good guess")
    else:
        print("Bad guess")
        attempts_left -= 1
    # Display current status
    display_words = ""
    for letter in secret_word:
        if letter in guessed_words:
            display_words += letter + " "
        else:
            display_words += "_" 
    print(display_words.strip())
        
        #Check win condition
    if "_" not in display_words:
        print("🎉 You win! The word was:", secret_word)
        break
    if attempts_left == 0:
        print("💀 You lose! The word was:", secret_word)

