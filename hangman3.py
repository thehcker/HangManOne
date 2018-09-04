import random

def printHang(n):
    gal = [['---- '],
           ['|  | '],
           ['|    '],
           ['|    '],
           ['|    ']]
    if n < 6:
        gal[2] = ['|  o ']
    if n < 5:
        gal[3] = ['| /  ']
    if n < 4:
        gal[3] = ['| / \\']
    if n < 3:
        gal[3] = ['| /|\\']
    if n < 2:
        gal[4] = ['| /  ']
    if n < 1:
        gal[4] = ['| / \\']
    for i in gal:
        print(''.join(i))

def randomWord():
    f = open('sowpods.txt', 'r')
    words = f.readlines()
    guessWord = words[int(random.random()*len(words))].strip()
    return guessWord

if __name__ == '__main__':

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
                    
        if guesses > 0:
            print('You\'re God damn right Champ!, \nit\'s ' + guessWord + '.')
        else:
            print('You lost. Looser.')

        if input('Play again? (Y//N):').upper() == 'N':
            break
       