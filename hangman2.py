import random

if __name__ == '__main__':

    print('Welcome to Hangman!')
    
    f = open('sowpods.txt', 'r')
    words = f.readlines()
    guessWord = words[int(random.random()*len(words))].strip()
        
    guessed = list('_'*len(guessWord))

    while list(guessWord) != guessed:
        print(' '.join(guessed))
        guessLetter = input('Guess your letter: ').upper()
        if guessLetter not in guessWord:
            print('Incorrect!')
        else:
            i = 0
            while i < len(guessWord):
                if list(guessWord)[i] == guessLetter:
                    guessed[i] = guessLetter
                i += 1

    print('You\'re God damn right, it\'s ' + guessWord + '.')