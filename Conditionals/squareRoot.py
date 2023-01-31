def average(a , b):
    return (a + b) / 2

def squareRoot(num, low, high):
    '''Finds the square root of num by
     playing the number guessing game
     strategy by guessing over the range
     from "low" to "high"'''
    for i in range(20):
        guess = average(low, high)
        if guess**2 == num:
            high = guess
        else:
            low = guess
    print(guess)