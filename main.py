import random
from word_list import hangman_list
from logo import logo
from stages import stages

# Display the logo
print(logo)

lives = 6

chosen_word = random.choice(hangman_list)

print(chosen_word)  # For testing purposes, remove or comment out in the final version

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"You have {lives}/6 lives")
    guessed = input("Please guess a letter: ").lower()
    print(guessed)

    if guessed in correct_letters:
        print(f"You have already guess {guessed}")

    display = ""
    for letter in chosen_word:
        if guessed == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guessed not in chosen_word:
        lives -= 1
        print(f"You guessed {guessed}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"You lose! It was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives])
