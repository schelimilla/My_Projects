import turtle
import random

f = open("swordle_wordbank.txt", "r")
content = f.read()
wordbank = content.splitlines()

word = random.choice(wordbank)
# word = "search"
word_as_list = []
for letter in word:
    word_as_list.append(letter)

s = turtle.Screen()
t = turtle.Turtle()

t.width("2")

t.penup()
t.goto(-20, 210)
t.pendown()
style = ("Courier", 35, "bold")
t.write("SWORDLE", font=style, align="center")

def draw_square():
    for i in range(4):
        t.forward(40)
        t.left(90)

def draw_row():
    for i in range(6):
        draw_square()
        t.penup()
        t.backward(60)
        t.pendown()

#Drawing boxes

t.speed(50)
t.penup()
t.goto(0, 0) #modified line
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.pendown()
starting_x = -150
starting_y = 200
for i in range(1, 9):
    draw_row()
    t.penup()
    t.goto(starting_x, starting_y - 50*i)
    t.pendown()

#User interaction

def exact_pos(x, y, mult):
    t.penup()
    t.goto(x + 80 + 60*mult, y + 40)
    t.pendown()
    t.fillcolor("lime green")
    t.begin_fill()
    draw_square()
    t.end_fill()
def letter_exists(x, y, mult):
    t.penup()
    t.goto(x + 80 + 60 * mult, y + 40)
    t.pendown()
    t.fillcolor("gold")
    t.begin_fill()
    draw_square()
    t.end_fill()
def letter_doesnt_exist(x, y, mult):
    t.penup()
    t.goto(x + 80 + 60 * mult, y + 40)
    t.pendown()
    t.fillcolor("dark gray")
    t.begin_fill()
    draw_square()
    t.end_fill()

def write(x, y):
    t.penup()
    t.goto(x + 60 * (i + 1), y)
    t.pendown()
    style = ("Courier", 25, "bold")
    t.write(guess_as_list[i], font=style, align="center")

game_over = False
attempt = 0
while game_over == False:
    guess = ""
    while len(guess) != 6:
        guess = turtle.textinput("Swordle", "Guess a word!")
    guess_as_list = []
    for letter in guess:
        guess_as_list.append(letter)
    attempt += 1
    if attempt == 1:
        x_pos = -230
        y_pos = 160
    if attempt == 2:
        x_pos = -230
        y_pos = 110
    if attempt == 3:
        x_pos = -230
        y_pos = 60
    if attempt == 4:
        x_pos = -230
        y_pos = 10
    if attempt == 5:
        x_pos = -230
        y_pos = -40
    if attempt == 6:
        x_pos = -230
        y_pos = -90
    if attempt == 7:
        x_pos = -230
        y_pos = -140
    if attempt == 8:
        x_pos = -230
        y_pos = -190
        # game_over = True


    # for i in range(6):
    #     if guess_as_list[i] == word_as_list[i]:
    #         exact_pos(x_pos, y_pos, i)
    #     elif guess_as_list[i] in word_as_list:
    #         letter_exists(x_pos, y_pos, i)
    #     elif guess_as_list[i] not in word_as_list:
    #         letter_doesnt_exist(x_pos, y_pos, i)
    #     write(x_pos, y_pos)
    #     if guess == word:
    #         game_over = True

    word_letter_freq = {}
    copy = {}
    for l in word_as_list:
        f = word.count(l)
        if l not in word_letter_freq:
            word_letter_freq[l] = f
        else:
            word_letter_freq[l] += f
    guess_letter_freq = {}
    for l in guess_as_list:
        f = word.count(l)
        if l not in guess_letter_freq:
            guess_letter_freq[l] = f
            copy[l] = f
        else:
            guess_letter_freq[l] += f
            copy[l] += f

    exact = False
    for i in range(6):
        match = False
        guess_letter = guess_as_list[i]
        if guess_letter not in word_as_list:
            letter_doesnt_exist(x_pos, y_pos, i)
        if guess_letter in word_as_list:
            if guess_letter_freq[guess_letter] > word_letter_freq[guess_letter]:
                # match = False
                if guess_as_list[0] == word_as_list[0] == guess_letter or guess_as_list[1] == word_as_list[1] == guess_letter or guess_as_list[2] == word_as_list[2] == guess_letter or guess_as_list[3] == word_as_list[3] == guess_letter or guess_as_list[4] == word_as_list[4] == guess_letter or guess_as_list[5] == word_as_list[5] == guess_letter:
                    letter_doesnt_exist(x_pos, y_pos, i)
                    match = True
                if copy[guess_letter] >= guess_letter_freq[guess_letter] and match == False:
                    letter_exists(x_pos, y_pos, i)
                if copy[guess_letter] < guess_letter_freq[guess_letter]:
                    letter_doesnt_exist(x_pos, y_pos, i)
                if guess_as_list[i] == word_as_list[i]:
                    exact_pos(x_pos, y_pos, i)
                copy[guess_letter] -= 1
                match = False

                # else:
                #     letter_exists(x_pos, y_pos, i)
            else:
                if guess_as_list[i] == word_as_list[i]:
                    exact_pos(x_pos, y_pos, i)
                else:
                    letter_exists(x_pos, y_pos, i)





        # if guess_as_list[i] == word_as_list[i]:
        #     exact_pos(x_pos, y_pos, i)
        # elif guess_as_list[i] in word_as_list:
        #     letter_exists(x_pos, y_pos, i)
        # elif guess_as_list[i] not in word_as_list:
        #     letter_doesnt_exist(x_pos, y_pos, i)
        write(x_pos, y_pos)
        if guess == word:
            game_over = True


    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 2:
    #     x_pos = -230
    #     y_pos = 110
    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 3:
    #     x_pos = -230
    #     y_pos = 60
    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 4:
    #     x_pos = -230
    #     y_pos = 10
    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 5:
    #     x_pos = -230
    #     y_pos = -40
    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 6:
    #     x_pos = -230
    #     y_pos = -90
    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 7:
    #     x_pos = -230
    #     y_pos = -140
    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 8:
    #     x_pos = -230
    #     y_pos = -190
    #     copy_word_as_list = word_as_list
    #     for i in range(6):
    #         if guess_as_list[i] == word_as_list[i]:
    #             exact_pos(x_pos, y_pos, i)
    #         elif guess_as_list[i] in copy_word_as_list:
    #             letter_exists(x_pos, y_pos, i)
    #             copy_word_as_list.remove(guess_as_list[i])
    #         elif guess_as_list[i] not in word_as_list:
    #             letter_doesnt_exist(x_pos, y_pos, i)
    #         write(x_pos, y_pos)
    #         if guess == word:
    #             game_over = True
    # if attempt == 8:
    #     game_over = True

# if game_over == True and attempt != 8:
#     style = ("Comic Sans MS", 30, "bold")
#     t.color("hot pink")
#     t.penup()
#     t.goto(0, -250)
#     t.write("You got it right in " + str(attempt) + " tries!", font=style, align="center")
# else:
#     style = ("Comic Sans MS", 30, "bold")
#     t.color("hot pink")
#     t.penup()
#     t.goto(0, -250)
#     t.write("The correct word was " + word, font=style, align="center")

if game_over == True:
    style = ("Comic Sans MS", 30, "bold")
    t.color("hot pink")
    t.penup()
    t.goto(0, -250)
    t.write("You got it right in " + str(attempt) + " tries!", font=style, align="center")
elif attempt == 8:
    style = ("Comic Sans MS", 30, "bold")
    t.color("hot pink")
    t.penup()
    t.goto(0, -250)
    t.write("The correct word was " + word, font=style, align="center")


s.exitonclick()

#IF USER GETS WORD RIGHT ON 8TH (LAST) TRY, PROGRAM DOESN'T ACKNOWLEDGE IT! SAYS THE CORRECT WORK WAS ... INSTEAD OF SAYING YOU GUESS IT CORRECTLY IN 8 TRIES