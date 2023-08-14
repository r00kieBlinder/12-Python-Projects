import random

'''
random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
'''

## Guess the NUmber(Computer)

def guess(x):
    random_number = random.randint(1, x<=10)
    guess = 0
    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and 10: '))
        if guess < random_number:
            print('Sorry, guess again, Too low')
        elif guess > random_number:
            print('Sorry, guess again, Too high')
        
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!')

# guess(10)




## Guess the Number(user)

def computer_guess(x):
    low = 1 
    high = x 
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)? : ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess - 1

    print(f'Yay! The Computer guessed your number, {guess}, correctly!')



# computer_guess (100)




# with this comment i'm just experimenting github