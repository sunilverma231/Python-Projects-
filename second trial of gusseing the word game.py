secret_word = "sunil"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != guess_count and not out_of_guess:
    if guess_count < guess_limit:
        guess = input ("Enter the Guess: ")
        guess_count += 1
    else: out_of_guess = True

    if out_of_guess:
       print("YOu ran out of guess, You Loose!")
    else:
       print ("you win")
