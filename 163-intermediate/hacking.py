import random
import urllib2

# Create dictionary
words = []
for line in urllib2.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt"):
    words.append(line)


# Could be replaced by just checking the size
def fill(guess, answer):
    # Fill guess or answer to avoid out of range error
    if (guess < answer):
        for i in range(0, len(answer) - len(guess)):
            guess += "*"
    elif (guess > answer):
        for i in range(0, len(guess) - len(answer)):
            answer += "*"

def terminal():

    # Words to be presented to the player
    possibilities = []
    for i in range(0, 5):
        possibilities.append(words[random.randint(0, len(words))])
        print possibilities[i],

    # Choose word to be guessed
    answer = possibilities[random.randint(0, 4)]
    print answer
    
    # Test guess against answer
    tries = 5
    for i in range(0, tries):
        # Guess
        print("You have %d tries" %(tries-i))
        guess = raw_input("Guess: ")
        fill(guess, answer)
        correct = 0
        for i in range(0, len(guess)):
            if (guess[i] == answer[i]):
                correct += 1

        if (correct == len(answer) - (len(answer) - len(guess))):
            print("You guessed right!")
            return
        else:
            print("You guessed %d characters right!" % correct)
    print("Game over!")

terminal()
