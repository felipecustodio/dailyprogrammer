import random
import urllib2

def fill(guess, answer):
    # Fill guess or answer to avoid out of range error
    if (guess < answer):
        for i in range(0, len(answer) - len(guess)):
            guess += "*"
    elif (guess > answer):
        for i in range(0, len(guess) - len(answer)):
            answer += "*"

# Create dictionary
words = []
for line in urllib2.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt"):
    words.append(line)

answer = list(words[random.randint(0, len(words))])

# Initialize hidden string
hidden = answer[:]
for i in range(0, len(answer)):
    hidden[i] = "_"

correct = 0
tries = 5

# Game loop
while tries > 0 and (correct != len(answer) - 1):
    print "".join(hidden)
    print "You have %d tries" % tries
    guess = raw_input("Guess: ")
    if guess in answer:
        correct += 1
        for i in range(0, len(answer) - 1):
            if answer[i] == guess:
                hidden[i] = guess
    else:
        tries -= 1

# Victory check
print "Game over"
if (correct == len(answer) - 1):
    print "You won!"
else:
    print "You lose!"