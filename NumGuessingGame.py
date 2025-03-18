# Deductive Logic Game - Guess the Secret Number

import random

print("Welcome to the Number Guessing Game!")

while True:
    user_input = input("Guess any 3-digit random number: ")
    if len(user_input) != 3 or not user_input.isdigit():
        print("Invalid input! Only 3-digit integers are allowed.")
    else:
        user_input = int(user_input)
        break

secret_number = random.randint(100, 999)

for i in range(10, 0, -1):
    if user_input == secret_number:
        print("Congratulations! You have guessed the correct number ✔️✔️✔️.")
        break
    elif user_input // 100 == secret_number // 100:
        print("Umm! Much closer. ✔️❌❌")
    elif user_input // 10 == secret_number // 10:
        print("Umm! Closer. ✔️✔️❌")
    else:
        print("Oops! Try again. ❌❌❌")
    
    if i > 1:
        print(f'{i-1} attempts left.')
        user_input = int(input("Guess again: "))
    else:
        print("No attempts left. Game over!")