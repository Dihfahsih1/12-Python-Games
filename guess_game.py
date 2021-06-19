import random    

def computer_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback!= 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correctly (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Congrats, The computer guessed the correctly your number, {guess}, ')
computer_guess(30)

    