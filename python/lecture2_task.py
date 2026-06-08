print("Welcome to the Number Guessing Game!")

correct_number = 9 
guess = int(input("Guess the number from 1 to 10: "))
attempts = 7
for attempt in range(1, attempts):
    if guess == correct_number:
        print("Congratulations! You guessed the number.")
        break
    elif 1 <= guess <= 10:
        print("Sorry, that's not the correct number. Try again!")
        guess = int(input("Guess the number from 1 to 10: "))
    else:    
        print("Invalid input. Please enter a number between 1 and 10.")
        guess = int(input("Guess the number from 1 to 10: "))
    continue
else:
    print("Sorry, you've used all your attempts. The correct number was", correct_number)