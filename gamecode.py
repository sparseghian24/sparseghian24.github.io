#pseudo code (steps)
# 1) loop through the maximum number of turns around
# - how many turns/wrong guesses is user allowed -->  #   6? (until hangman man runs out of body parts- 2 # 
#   hands/head/body/2 legs)
# - as long as u get them right u continue to get 
#   chances but once u get 6 wrong game is over 

# 2) get a guess from the player 
# 3) check guess (see if letter is in word)
# - if letter is in word, add it to the word
# - if letter not in word, add to number of wrong counts and
# 4) check if word is complete 
# - if word is complete, break out of loop (yay u won word is complete)
# 5) if out of tries and word is not complete, break out of loop and say u lost (tell user what the word actualy was)

#list of random words
import random

names = ["soleen", "jed", "ananya", "anoush", "conrad", "daniel", "dylan", "elizabeth", "giorgio", "harout", "jacob", "jonah", "jonathan", "kubra", "kyle", "lucas", "natalia", "oscar", "tenley", "wesley", "zachary"]
countries = ["argentina", "armenia", "brazil", "canada", "lebanon", "syria", "kuwait", "egypt", "australia", "austria", "germany", "france", "netherlands", "switzerland", "italy", "uruguay", "georgia", "iraq", "jordan", "iran"]
foods = ["pizza", "burger", "pasta", "sushi", "tacos", "chicken", "fries", "steak", "salad", "chips", "rice", "noodles", "soup", "cake", "ice cream", "candy", "cookies"]

def choose_theme():
    while True:
        print("Choose a theme: names, countries, or foods")
        theme = input().lower()

        if theme in ["names", "countries", "foods"]:
            if theme == "names":
                return names
            elif theme == "countries":
                return countries
            else:
                return foods
        else:
            print("Error: please enter a valid theme (names, countries, or foods)")

def display_word(secretword, lettersGuessed):
    display = ''
    for letter in secretword:
        if letter in lettersGuessed:
            display += letter 
        else: 
            display += '_'
    return display 


def play_hangman():
    word_list = choose_theme()
    secretword = random.choice(word_list)
    lettersGuessed = ""
    wrongGuesses = []
    rightGuesses = []

    failureCount = 6
    score = 0

    hangman_stages = [
         """
        -----
        |   |
            |
            |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
        ---------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        ---------
        """
    ]

    while failureCount > 0:
        print(hangman_stages[6 - failureCount])
        print(f"Wrong guesses: {', '.join(wrongGuesses)}")
        print(f"Right guesses: {', '.join(rightGuesses)}")
        print(display_word(secretword, lettersGuessed))
        guess = input("Enter a letter: ").lower()
        if guess in lettersGuessed:
            print("You've already guessed that letter. Try again.")
            continue
        lettersGuessed += guess
        if guess in secretword:
            rightGuesses += guess
            if all(letter in lettersGuessed for letter in secretword):
                print(f"Congratulations! The secret word was: {secretword}. You won!")
                break
        else:
            wrongGuesses.append(guess)
            failureCount -= 1
        if failureCount == 0:
            print(hangman_stages[6])
            print(f"Game over, you lost. The word was: {secretword}.")
            break
        print(f"Your score is {score}")
        
if __name__ == "__main__":
    play_hangman()


















