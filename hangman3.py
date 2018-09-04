import random
# A function that prints the hangman using ASCII whenever called
def printHang(n):
    hang = [['---- '],
           ['|  | '],
           ['|    '],
           ['|    '],
           ['|    ']]
    if n < 6:
        hang[2] = ['|  o ']
    if n < 5:
        hang[3] = ['| /  ']
    if n < 4:
        hang[3] = ['| / \\']
    if n < 3:
        hang[3] = ['| /|\\']
    if n < 2:
        hang[4] = ['| /  ']
    if n < 1:
        hang[4] = ['| / \\']
    for i in hang:
        print(''.join(i))
#Saves randon word from sowpods as guessWord.
#Returns random word from sowpods dictionary

def randomWord():
    f = open('sowpods.txt', 'r')
    words = f.readlines()
    guessWord = words[int(random.random()*len(words))].strip()
    return guessWord

if __name__ == '__main__':
# Loops through the proram as long as the game is running
    while True:
        print('Welcome to Hangman!')
        guessWord = randomWord()
        guesses = 6
        guessed = list('_'*len(guessWord))
        used = set()

        while list(guessWord) != guessed and guesses > 0:
            print(' '.join(guessed))
            guessLetter = input('Guess your letter: ').upper()
            if guessLetter in used:
                print("Letters already guessed",used)
                print('You already tried \''+guessLetter+'\'.')
                continue
            used.add(guessLetter)
            if guessLetter not in guessWord:
                guesses -= 1
                printHang(guesses)
            else:
                i = 0
                while i < len(guessWord):
                    if list(guessWord)[i] == guessLetter:
                        guessed[i] = guessLetter
                    i += 1
        #Win or lose condition (display having no underscores left in it); breaks loop.
        if guesses > 0:
            print('You\'re God damn right Champ! \nit\'s ' + guessWord + '.')
        else:
            print('You lost. Looser.')
        #Prompts the user to either start another game or exit from the game.
        if input('Play again? (Y//N):').upper() == 'N':
            break
       