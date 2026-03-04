import random

# List of names
names = ["Jaweid", "Abazar", "Ali", "Reza", "Sara", "Neda", "Hamed", "Maryam", "Omid", "Parisa"]

# Select one name randomly
selected_name = random.choice(names)
selected_name_lower = selected_name.lower()  # برای مقایسه

guess_count = len(selected_name)
guessed_letters = []
display_list = ["_"] * len(selected_name)

print("🎮 Welcome to the Hangman Game!")
print(" ".join(display_list))

while guess_count > 0:
    guess = input(f"\nRemaining guesses: {guess_count}\nEnter a letter: ").lower()

    # Check if input is valid
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter only ONE valid letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in selected_name_lower:
        # Update display_list with correct guesses (show in uppercase)
        for index, char in enumerate(selected_name_lower):
            if char == guess:
                display_list[index] = selected_name[index].upper()
        print("✅ Good job!")
    else:
        guess_count -= 1
        print("❌ Wrong guess!")

    print(" ".join(display_list))

    # Check win condition
    if "_" not in display_list:
        print(f"\n🎉 Congratulations! You guessed the name: {selected_name.upper()}")
        break

# Lose condition
if guess_count == 0 and "_" in display_list:
    print(f"\n💀 Game Over! The name was: {selected_name.upper()}")