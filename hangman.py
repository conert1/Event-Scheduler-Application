#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    f = open(file_name, 'r')    
    file_name = f.readlines()
   
    f.close()
    return file_name


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    #selecting a random word from the list
    r_word = random.randint(0, len(words)-1)

    #random number generator
    ra = random.randint(0, len(words[r_word])-2)
    h_letter = words[r_word].replace(words[r_word][ra], "_")
    
    print("Guess the word: " + h_letter)
    return words[r_word]


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    ans = input("Guess the missing letter: ")
    return 'TODO'


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

