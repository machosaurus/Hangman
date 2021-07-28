#######################################
#Hangman Game made by MachieTabaru
#2021
#######################################

def head():
    print("  ______")
    if error == -2: 
        print("        | ")
        print("        |\n        |\n        |")
    elif error == -1: 
        print("  |     | ")
        print("        |\n        |\n        |")
    else:
        print("  |     | ")
        print(hangman[0],"    |")
        if error == 0:
            print("        |\n        |")

def body():
    head()
    if error == 1:
        print(' ', hangman[2], "    |")
        print("        |")
    elif error == 2:
        print(hangman[1]+hangman[2],"    |")
        print("        |")
    elif error == 3:
        print(hangman[1]+hangman[2]+hangman[3],"   |")
        print("        |")
    else:
        print(hangman[1]+hangman[2]+hangman[3],"   |")

def legs():
    body()
    if error ==  4:
        print(hangman[4],"     |")
        print("        |")
        print("Last Wrong Guess Left!")
    else:
        print(hangman[4],hangman[5],"   |")
        print("        |")
        print("Sorry! You didn't get it in time to save the man.")
        print("Your word was:", word)
        print("Better luck next time!\n\n")
        exit()

hangman = ['  O',' /','|','\\',' /','\\']
draw = {
       -2 : head,
       -1 : head,
        0 : head,
        1 : body,
        2 : body,
        3 : body,
        4 : legs,
        5 : legs,
}

def checkLetterinWord(letter):
    if letter in word:
        #print("CONTAINS", found)
        foundIndices = [];
        while found.count(letter):
            #print('found: ', found.index(letter))
            spaces[found.index(letter)] = ' ' + letter
            #print(*spaces, sep='')
            found[found.index(letter)] = ''
            #print("spaces", spaces)
            #print('N:', found)

            if not " _" in spaces:
                print("\n",*spaces, sep = '')
                win()
        return True

    return False
       

def checkRepeat(letter):
    if (letter in wrongGuesses) or ((' ' + letter) in spaces):
        return True
    else:
        return False


def win():
    print("\n>>> CORRECT!!!")
    print("Thanks for Playing!\nCome back for another challenge you Brainiac!\n\n")
    exit()
################################################################################
import random

ist = [] 

with open('engmix.txt','r', encoding='unicode_escape') as f:
    word = f.readline().strip()
    while word:
        word = f.readline().strip()
        ist.append(word.upper())
        #if(word == 'ACID'):
            #   word = ''

var = random.randint(0,len(ist))
word = ist[var]
error = -2
hangman = ['  o',' /','|','\\',' /','\\']

#print('\n\nWord #',var,word) #uncomment line to see answer before each play.
print('=================================')
print(">>> Hey, What's Hangin? Wanna Play Hangman??")
print("\n")

found = []
spaces = []
wrongGuesses = []

for item in word:
    spaces.append(' _')
    found.append(item)
print(*spaces, sep = '')


while True:
    if not len(wrongGuesses) == 0 :
        print("\nPrevious Guesses: ",*wrongGuesses, sep=' ')
    letter = input('\n>>> Guess a Letter, Any Letter: ')
    letter = letter.upper()
    
    if len(letter) > 1 or not letter.isalpha():
        print("Please enter a letter.")
        print("\n",*spaces, sep = '')

    elif checkRepeat(letter):
        print("You've already guessed this letter. Guess another.")
        print("\n",*spaces, sep = '')

    else:
        if checkLetterinWord(letter):
            print('\nYou Guessed correctly!')
            print("\n",*spaces, sep = '')
        else:
            print("\nWRONG! Guess Again.")
            draw[error]()
            error+= 1
            wrongGuesses.append(letter)
            print("\n",*spaces, sep = '')
                
    

            
        

