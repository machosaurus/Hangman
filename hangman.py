#######################################
#Hangman Game made by M.Tabaru
#2021
#######################################

def head():
    print("  ______")
    print("  |     | ")
    print(hangman[0],"    |")
    if error == 0:
        print("        |")
        print("        |")

def body():
    head()
    if error == 1:
        print(' ',hangman[2],"    |")
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
draw = {0 : head,
        1 : body,
        2 : body,
        3 : body,
        4 : legs,
        5 : legs,
}

def win():
    print("\n>>> CORRECT!")
    print("I can't believe you got a word correctly out of the list of such fancy but useless words I just grabbed through some list.")
    print("Thanks for Playing!\nCome back for another challenge you Brainiac!\n\n")
    exit()

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

################################################################################
import random

ist = [] 

with open('sowpods.txt','r') as f:
        word = f.readline().strip()
        while word:
            word = f.readline().strip()
            ist.append(word)
            if(word == 'ACID'):
                word = ''

var = random.randint(0,len(ist))
word = ist[var]
error = 0
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

    letter = input('\n>>> Guess a Letter, Any Letter: ')
    letter = letter.upper()
    
    if len(letter) > 1 or not letter.isalpha():
        print("Please enter a letter.")
    elif checkRepeat(letter):
        print("You've already guessed this letter. Guess another.")
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
                
    

            
        

