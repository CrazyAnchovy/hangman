#MBowenCPT135

#hangMan

import random
import os




def incorrectGuessAttempts0():
    print("""            +---+
            |   |
                |
                |     BEHOLD THE GALLOWS OF JUSTICE
                |
                |
          =========""")
def incorrectGuessAttempts1():
    print("""            +---+
            |   |
            0   |
                |     BEHOLD THE GALLOWS OF JUSTICE
                |
                |
          =========
          sufferin' sucatash! they put the noose on him! HE'S INNOCENT!""")
def incorrectGuessAttempts2():
    print("""            +---+
            |   |
            0   |
            |   |     BEHOLD THE GALLOWS OF JUSTICE
                |
                |
          =========
          good heavens to betsy & good lord miss hannah! they moved his body under him!""")
def incorrectGuessAttempts3():
    print("""            +---+
            |   |
            0   |
            |\  |     BEHOLD THE GALLOWS OF JUSTICE
                |
                |
          =========
          may the almighty watch upon us! they've got one arm out for a-tyin' up!""")
def incorrectGuessAttempts4():
    print("""            +---+
            |   |
            0   |
           /|\  |     BEHOLD THE GALLOWS OF JUSTICE
                |
                |
          =========
          now they've got the second arm! i hope the reverend is here for this mans last rights!""")
def incorrectGuessAttempts5():
    print("""            +---+
            |   |
            0   |
           /|\  |     BEHOLD THE GALLOWS OF JUSTICE
            \   |
                |
          =========
          i aint never seen a man so closed to bein' hanged! he'll be saved god willin and the creek don't rise!""")
def incorrectGuessAttempts6():
    print("""            +---+
            |   |
            0   |
           /|\  |     BEHOLD THE GALLOWS OF JUSTICE
           /\   |
                |
          =========
          poor feller never hurt noone. just couldn't spell is all...rip stick dude""")


def main():
    secretWord=[]
    guessedWord=[]
    guessedWrongList=[]
    correctGuesses=[]                                                                    
    correctLetters = 0
    incorrectGuessAttempts=0
    playAgain = 'y'
    while playAgain == 'y':
        with open('wordList.txt', 'r') as wordList:                                      #if the player plays again, return to the beginning of the wordlist
            wordList.seek(0)
        
        with open('wordList.txt', 'r') as wordList:                                      #open the file in readMode
            i=0                                                                          #thanks to /u/commandlineuser for reminding me that after the loop, there are no more lines to read
            for lines in wordList:                                                       #count the lines of the file to create a range for randint()
                i+=1
        
        with open('wordList.txt', 'r') as wordList:                                      #reopen the file
            wordSelect = random.randint(0,i)                                             #use i from the previous open        
            secretWord = wordList.readlines()[wordSelect]                                #get the line(which is one word)         
            
        for letters in range (len(secretWord)-1):                                        #making the blanks to guess. none of the letters have been guessed yet.
            guessedWord.append('_ ')
        
        #print(secretWord)                                                               #incuded for debugging
        print("Welcome to Hang Man!")
        print("The exciting word game of life or death!")
        print("Will you guess the letters and save a mans life?")
        print("Or will you watch an innocent man die!?\n")
        incorrectGuessAttempts0()                                                         #start by drawing the empty gallows
    
    
        print('the secret word is ', end=' ')                                             #printing out the blanks in guessedWord. nothing has been guessed at this point
        for letter in guessedWord:                                                        #so it is all blanks
            print(letter, end=' ')
            
        while correctLetters < len(secretWord)-1 and incorrectGuessAttempts < 6:          #the conditions of the loop: not 6 misses, and all letters not guessed
            guessedLetter = input('please guess a letter!')
            
            if guessedLetter not in 'abcdefghijklmnopqrstuvwxyz':                          #make sure it is a letter
                print("Hey! Ya yella-bellied scoundrel! We only use words with only letters 'round these parts. Try again.")
            elif guessedLetter in secretWord:                                              #checks just for statement
                print('\nyes! that letter is in the word!')
                correctLetters +=1                
            elif guessedLetter in guessedWrongList:                                        #checks just for statement
                print('\nya already done guessed that one! you tryin to kill an innocent man?!')
            else:                                                                          #this would be a wrong guess
                print('this man is one step closer to dying because of you! \n')
                incorrectGuessAttempts += 1                                                #increments incorrectGuessAttempts
                
            
            if incorrectGuessAttempts == 0:                                                #prints the proper gallows depending on
                incorrectGuessAttempts0()                                                  #how many incorrect/correct guesses
            elif incorrectGuessAttempts == 1:
                incorrectGuessAttempts1()
            elif incorrectGuessAttempts == 2:                                              #this should have been a list or dict
                incorrectGuessAttempts2()
            elif incorrectGuessAttempts == 3:
                incorrectGuessAttempts3()
            elif incorrectGuessAttempts == 4:
                incorrectGuessAttempts4()
            elif incorrectGuessAttempts == 5:
                incorrectGuessAttempts5()
            elif incorrectGuessAttempts == 6:
                incorrectGuessAttempts6()
            
            for i in range (len(secretWord)-1):                                           #this for loop is going to print out the word with some blanks
                if guessedLetter == secretWord[i]:                                        #checks each letter to see if it matches the guess
                    guessedWord.pop(i)                                                    #pops out the spot which is currently a '_'
                    guessedWord.insert(i, guessedLetter)                                  #inserts the guessedLetter in the spot
                                                                                          #keeps track of the amount of correct guesses to end loop when 
                
            if guessedLetter not in secretWord and guessedLetter not in guessedWrongList: #this is going to keep track of the wrong letters
                guessedWrongList.append(guessedLetter)
            print ("here is what done guessed right so far: " + ''.join(guessedWord))     #prints out the secret word in a legible format
        
            print ("and here's what ya AINT got: " + ''.join(guessedWrongList))           #prints the missed letters for reference
              
        if incorrectGuessAttempts >= 6:                                                   #when incorrectGuessAttempts gets to 6...game over
            print('this man was hanged by the neck until dead')
            print('the secret word was: ' + secretWord)
            
        elif correctLetters == (len(secretWord)-1):                                        #when all the letters are guessed...game won
            print("yay! this man was saved from a-hangin!")
        secretWord=[]                                                                      #reset my lists back to empty
        guessedWord=[]
        guessedWrongList=[]
        correctLetters = 0
        incorrectGuessAttempts=0           
        playAgain = input("would you like to play again?(y/n)")
        print('\n\n\n')
    input('hit enter to exit')
main()



    