import random    

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high')
#     print(f'Congrats, you have guessed the right number {random_number} correctly !!!')
# guess(10)

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

    