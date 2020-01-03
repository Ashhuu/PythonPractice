import random
listG = []
chances = 6
correct = 0
star = "*"
full_word = ""
print("Welcome to Hangman 1.0")
print("You have to guess a word and you have 6 chances available. Good Luck!\n")


def start():
    list_words = ['hospital', 'ambulance', 'holiday', 'carnival', 'mountain', 'station', 'airplane']
    choice_word = random.choice(list_words)
    return choice_word


status = 'play'
while status == 'play':
    word = start()
    while chances > 0:
        for i in range(0, len(word)):
            if correct == 0:
                full_word = full_word + "_"
            elif correct > 0:
                for j in range(0,len(listG)):
                    if i == listG[j]:
                        guess_letter = word[i]
                        break
                    else:
                        guess_letter = "_"
                full_word = full_word+guess_letter
        print(full_word)
        full_word = ""
        if len(word) == len(listG):
            print("\nThe word is '" + format(word) + "'")
            print("Congratulations! You Won!~")
            exit()
        guess = input("Guess the word:")
        found = 0
        for i in range(0, len(word)):
            if guess == word[i]:
                print("\nYou guessed correctly!")
                print("Remaining chances: " + format(chances))
                listG.append(i)
                correct = correct + 1
                found = found + 1
        if found == 0:
            print("\nWrong Guess")
            chances = chances - 1
            print("Remaining chances: " + format(chances))
    print("\nUnfortunately, you have lost.")
    play_again = input("Would you like to play again? Yes or No")
    if play_again.lower() == 'yes':
        status = 'play'
        chances = 6
        listG = []
    elif play_again.lower() == 'no':
        break

