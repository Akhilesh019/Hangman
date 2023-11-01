import random
from Words import words


chosen_word = random.choice(words)
word_length = len(chosen_word)
end_of_game = False

display = ["_" for i in range(len(chosen_word))]

lives = 6

from hangman_art import logo, stages

print(logo)
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was ,{chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won.")
        print(f"The word was ,{chosen_word}")

    print(stages[lives])
