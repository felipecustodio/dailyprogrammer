import random
import urllib2
# Create dictionary
words = []
for line in urllib2.urlopen("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt"):
    words.append(line)

def terminal():
    # Words to be presented to the player
    possibilities = []
    for i in range(0, 5):
        possibilities.append(words[random.randint(0, len(words))])
        print possibilities[i],  
    
    # Guess
    guess = raw_input("Guess: ")
    
    # Compare guess to list
    for i in range(0, len(possibilities) - 1):
        # Compare guess to words
        for j in range(0, len(possibilities[i]) - 1):
            points = len(possibilities[i])
            if (guess[j] == possibilities[i][j]):
                 print("Guessed right ;)")
        

terminal()




