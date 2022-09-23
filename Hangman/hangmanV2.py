import random

print("Welcome to HANGMAN!\n")
print("Rules:")
print("------")
print("1) Choose a category and guess a letter on each try")
print("2) If you think you know the word, you may enter a word instead of a letter")
print("3) If you give up and do not want to continue guessing, type 'answer' instead of guessing a letter\n")

f = open("wordbankV2.txt", "r")
content = f.read()
my_list = content.splitlines()

colors_list = my_list[0:13]
fruits_list = my_list[14:27]
flowers_list = my_list[28:39]
instruments_list = my_list[40:52]
animals_list = my_list[53:73]

choose = input("Select a category - animals, colors, flowers, fruits, instruments, random: ")
while choose != "animals" and choose != "colors" and choose != "flowers" and choose != "fruits" and choose != "instruments" and choose != "random":
    print("You have selected an invalid category - please choose again!")
    choose = input("Select a category - animals, colors, flowers, fruits, instruments, random: ")
if choose == "colors":
    my_list = colors_list
if choose == "fruits":
    my_list = fruits_list
if choose == "flowers":
    my_list = flowers_list
if choose == "instruments":
    my_list = instruments_list
if choose == "animals":
    my_list = animals_list

word = random.choice(my_list)
dash = "_".join(word) + "_"
display_word = dash[1:len(dash)+1:2]
print(display_word)

guessed_letters = []
counter = 0
while display_word != word:
    counter += 1
    guess_letter = input("Guess a letter: ")
    if guess_letter == "answer":
        print("The correct answer is " + word + "!")
        break
    if guess_letter == word:
        print("Good Job - you guessed the word correctly in " + str(counter) + " tries!")
        break
    for letter in guessed_letters:
        if guess_letter == letter:
            guess_letter = input("You already guessed this letter! Guess another letter: ")
    guessed_letters.append(guess_letter)
    a = guess_letter + "_"
    b = guess_letter + guess_letter
    dash = dash.replace(a, b)
    display_word = dash[1:len(dash) + 1:2]
    print(display_word)
    if display_word == word:
        print("Good Job - you guessed the word correctly in " + str(counter) + " tries!")