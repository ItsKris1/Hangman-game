

print('Hello, lets play Hangman!')
print('')


# Checks if the user input is number
check_int = True
while check_int:
    try:
        chances_to_fail = int(input('How many chances to fail?: '))
        check_int = False
    except ValueError:
        print('Only number is accepted')
        continue


# Checks if the user input consists only alphabetical letters with no special characters
check_isalpha = True
while check_isalpha:
    word_to_guess = input('Enter a single word to be guessed: ').lower()

    if not word_to_guess.isalpha():
        print('Only a word is accepted')
        continue
    else:
        check_isalpha = False


print('')
print('Lets enter names if you are done press Enter')


# Asks player names and puts them into the dictionary with
# Keys as names
# Values as lists - in the lists will be wrong guesses
players = {}

creating_players = True
while creating_players:
    pn = input('Enter name: ').capitalize()

    if pn in players:
        print(f'Name exists already. Enter another one please.')
        continue

    elif pn == '':
        creating_players = False

    else:
        players[pn] = []


print(players)
print('')
print('')
print('')
print('---------------------------------')
print('')
print('***GAME START***')


# Gives the user information on who are playing
player_names = [a for a in players.keys()]
print(f'Players:', (', '.join(player_names)))


print('')


# Replaces each character in the - word_to_guess - with '__ ' to make it hidden
# Lastly gets rid of the last whitespace
# Returns us hidden word
def make_hidden_word(wtg):
    wtg_to_dashes = len(word_to_guess) * '__ '
    hid_word = ' '.join(wtg_to_dashes.split(" "))
    return hid_word.rstrip()


# Inserts users correct guess to the hidden word
def insert_to_hidden_word(hid_word, wtg, letter):
    s_hidden_word = hid_word.split(" ")

    if wtg.count(letter) > 1:
        letter_pos = [idx for idx, char in enumerate(wtg) if char == letter]
        for i in letter_pos:
            s_hidden_word[i] = letter
    else:
        letter_pos = wtg.find(guess)
        s_hidden_word[letter_pos] = guess

    hid_word = ' '.join(s_hidden_word).rstrip()
    return hid_word.upper()


hidden_word = make_hidden_word(word_to_guess).lower()


# Checkpoint, which checks when the word is guessed
# You will see what its for further below
right_guesses = 0


# Game starts here
game_on = True
while game_on:
    for player in player_names:

        print('---------------------------------')
        print('')

        print(f'Word - [ {hidden_word} ]')

        ask_guess = True
        while ask_guess:

            guess = input(f'{player} enter a guess: ').lower()

            if not guess.isalpha():
                print('Invalid input. Please enter only letters')
                continue

            else:
                ask_guess = False

        print('')

        if guess in word_to_guess:
            right_guesses += 1

            print('**Correct**')
            print('')

            hidden_word = insert_to_hidden_word(
                hidden_word, word_to_guess, guess)

            # We make word_to_guess to uppercase because 'the_word' is also in Uppercase
            # Then we use .join to make it a normal string without any spaces
            # This way we can find out if the word has been found
            the_word = ''.join(hidden_word.split(' '))
            if the_word == word_to_guess.upper():

                print('---------------------------------')
                print('You\'ve won!')
                print(f'The word was: {the_word.upper()}')
                print('Thanks for playing')

                game_on = False
                exit()

        else:
            print('**False**')

            players[player].append(guess)

            # Shows player wrong answers so far, take it as a tracker
            player_misses = ', '.join(players[player]).upper()
            print(f'{player}: [{player_misses}]')

            print('')

            # Example - chances_to_fail = 2
            # We know that players wrong guesses will be stored in the lists in 'Players' dictionary
            # If wrong guesses and chances to fail are equal it means the player has lost
            if len(players[player]) == chances_to_fail:
                print(f'!!!{player} out!!!')

                del players[player]

                # If there are no players in 'Players' dictionary
                if len(players) <= 0:
                    print('')
                    print('---------------------------------')
                    print('')
                    print('@@@@@ GAME OVER @@@@@')
                    print('Thanks for playing')
                    game_on = False
                    exit()

                print('')

                # If a player has fallen out, shows how many are left
                player_names = [a.capitalize() for a in players.keys()]

                print('---------------------------------')
                print(f'Players left:', (', '.join(player_names)))
