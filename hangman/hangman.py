import random

languages = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')


def hangman(language):
    secret_word = random.choice(language)
    display = '-' * len(secret_word)
    count = 8
    temp = ''
    while True:
        new_display = list(display)
        if count == 0:
            print("You are hanged!")
            print()
            break
        elif display == secret_word:
            print(f'You guessed the word {display}!')
            print('You survived!')
            print()
            break
        else:
            print()
            print(display)
            guess = input('Input a letter: ')
            if len(guess) != 1:
                print('You should input a single letter')
            else:
                if guess in temp:
                    print('You already typed this letter')
                else:
                    temp += guess
                    if guess.islower():
                        if guess in secret_word:
                            for i in range(len(secret_word)):
                                if secret_word[i] == guess:
                                    new_display[i] = guess
                                    display = ''.join(new_display)
                                # count -= 1
                        else:
                            print('No such letter in the word')
                            count -= 1
                    else:
                        print('It is not an ASCII lowercase letter')


while True:
    action = input('Type "play" to play the game, "exit" to quit: ')
    if action == 'play':
        hangman(languages)
    elif action == 'exit':
        break
