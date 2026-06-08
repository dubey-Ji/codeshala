secret_number = 17
max_attempt = 7
user_attempted = 0
start_number = 2
end_number = 20
print(f"Welcome to Guess Game\nYou have total {max_attempt} attempts to guess the number. The number range is between {start_number} to {end_number}")
while (user_attempted != max_attempt):
    print(f"Attempts pending {max_attempt - user_attempted}")
    user_guess_number = int(input("Guess a number: "))
    if user_guess_number == secret_number:
        print("You have successfully guess the number. Congrats!!")
        break
    elif user_guess_number < start_number or user_guess_number > end_number:
        print(f"You have guessed number out of the range. Range is between {start_number} to {end_number}")
    else:
        print("Sorry wrong guess")
    user_attempted += 1
