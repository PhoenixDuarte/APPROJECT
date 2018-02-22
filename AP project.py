import random
def guesscolour():
    loop = True
    gess = 0
    print ("Guess what colour the program has selected. If you win, then the program stops. If you lose, you'll be trapped here forever.")
    print ("Your options are: Black, White, Orange, Red, Yellow, Pink, Brown, Blue, Green, Cyan, and Gray.")
    while loop == True:
        colour = random.choice(['Black','White','Orange','Red','Yellow','Pink','Brown','Blue','Purple','Green','Cyan','Gray'])
        print ("The colours have been scrambled! Guess a colour. Remember: If you guess wrong, you'll be retrying!")
        print 'You guessed' ,gess, 'times!'
        guess = raw_input('What do you guess? ')
        gess += 1
        if guess == colour:
                loop = False
                print ('You completed the challenge. Good work, you are free to go.')
                print ('You guessed a total of' ,gess, 'times!')  
                break