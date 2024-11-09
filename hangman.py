import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {0:("   "
                 ,"   "
                 ,"   "),
                1: (" o ",
                    "   ", 
                    "   "),
                2: (" o "
                  , " | "
                  , "   "),
                3: (" o ",
                    "/| ", 
                    "   "),
                4: ("  o ",
                    " /|\\",
                    "     "),
                5: ("  o ",
                    " /|\\",
                    " /   "),
                6: (" o",
                    "/|\\",
                    "/ \\")}
def display_name(wrong_guesses):
    for lines in hangman_art[wrong_guesses]:
        print(lines)

def display_hint(hint):
    print(f"The hint is {" ".join(hint)}")
    

def display_answer(answer):
    print(f"The answer is {answer}")



def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guesses = 0
    starter = True
    guessed_items_list = set()

    while starter:
        display_hint(hint)
        display_name(wrong_guesses)
        guess = input("Enter a letter: ")
        guesses += 1
        if guess in guessed_items_list:
            print("You have used this letter before you can't use it again.")
            continue
        if len(guess) != 1 or not guess.isalpha():
                print("Invalid.")
        guessed_items_list.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                
                if guess == answer[i]:
                    hint[i] = guess
                    
        if guess not in answer:
            wrong_guesses += 1

        if "_" not in hint:
            print("You win")
            break

        if wrong_guesses == len(hangman_art):
            print("You loose")
            break

        

                

    

if __name__ == "__main__":
    main()
