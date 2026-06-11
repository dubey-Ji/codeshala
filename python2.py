print("welcome in number guessing game")

correctnumber = 5 
attempt = 7 
for attempts in range (1,attempt+1):
    guess = int(input("guess number from 1 to 10"))
    if guess == correctnumber:
        print("congrats you win")
        break 
    elif 1<= correctnumber <=10:
        print ("you loose")
    elif 1< correctnumber <10:
     print("invalid input")
    else:
      print("you loose the game")
