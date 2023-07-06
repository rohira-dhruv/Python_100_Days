import random
import art
from words import word_list

chosen_word = random.choice(word_list)
length = len(chosen_word)
num_lives = 6
end_of_game = False

display_list = []
for _ in chosen_word:
    display_list.append('_')

print(art.logo)
print(f"The word is {chosen_word}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display_list:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        num_lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if num_lives == 0:
            end_of_game = True
            print("You lose.")
    else:
        for num in range(length):
            if guess == chosen_word[num]:
                display_list[num] = guess
        if "_" not in display_list:
            end_of_game = True
            print("You won.")

    print(f"{' '.join(display_list)}")
    print(art.stages[num_lives])
