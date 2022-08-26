import turtle
import time

s = turtle.Screen()
t = turtle.Turtle()

t.width("3")

t.speed(10)
t.penup()
t.left(90)
t.forward(150)
t.left(90)
t.pendown()
t.forward(150)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(150)

t.penup()
t.goto(-50, 150)
t.left(90)
t.pendown()
t.forward(300)
##
t.penup()
t.left(90)
t.goto(50, -150)
t.left(90)
t.pendown()
t.forward(300)
##
t.penup()
t.goto(-150, 50)
t.right(90)
t.pendown()
t.forward(300)
##
t.penup()
t.right(90)
t.goto(150, -50)
t.right(90)
t.pendown()
t.forward(300)
t.speed(6)

turn = 1
state = ["", "", "", "", "", "", "", "", ""]
winner = ""

player1 = turtle.textinput("Player Name", "Player1, enter your name!")
player2 = turtle.textinput("Player Name", "Player2, enter your name!")

def player(x, y):
    global turn
    global state
    global winner
    t.penup()
    t.goto(x, y)
    t.pendown()
    if turn % 2 == 1:
        color = "blue"
        if x < -50 and y > 50:
            state[0] = player1
            x_pos = -100
            y_pos = 120
        if x > -50 and x < 50 and y > 50:
            state[1] = player1
            x_pos = 0
            y_pos = 120
        if x > 50 and y > 50:
            state[2] = player1
            x_pos = 100
            y_pos = 120
        if x < -50 and y > -50 and y < 50:
            state[3] = player1
            x_pos = -100
            y_pos = 20
        if x > -50 and x < 50 and y > -50 and y < 50:
            state[4] = player1
            x_pos = 0
            y_pos = 20
        if x > 50 and y > -50 and y < 50:
            state[5] = player1
            x_pos = 100
            y_pos = 20
        if x < -50 and y < -50:
            state[6] = player1
            x_pos = -100
            y_pos = -80
        if x > -50 and x < 50 and y < -50:
            state[7] = player1
            x_pos = 0
            y_pos = -80
        if x > 50 and y < -50:
            state[8] = player1
            x_pos = 100
            y_pos = -80
    if turn % 2 == 0:
        color = "red"
        if x < -50 and y > 50:
            state[0] = player2
            x_pos = -100
            y_pos = 120
        if x > -50 and x < 50 and y > 50:
            state[1] = player2
            x_pos = 0
            y_pos = 120
        if x > 50 and y > 50:
            state[2] = player2
            x_pos = 100
            y_pos = 120
        if x < -50 and y > -50 and y < 50:
            state[3] = player2
            x_pos = -100
            y_pos = 20
        if x > -50 and x < 50 and y > -50 and y < 50:
            state[4] = player2
            x_pos = 0
            y_pos = 20
        if x > 50 and y > -50 and y < 50:
            state[5] = player2
            x_pos = 100
            y_pos = 20
        if x < -50 and y < -50:
            state[6] = player2
            x_pos = -100
            y_pos = -80
        if x > -50 and x < 50 and y < -50:
            state[7] = player2
            x_pos = 0
            y_pos = -80
        if x > 50 and y < -50:
            state[8] = player2
            x_pos = 100
            y_pos = -80
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(x_pos, y_pos)
    t.pendown()
    t.circle(20)
    t.end_fill()
    turn += 1
    determine_winner()

s.onclick(player)
# s.mainloop()


def determine_winner():
    global winner
    global turn
    if state[0] != "" and state[1] != "" and state[2] != "" and state[0] == state[1] == state[2]:
        winner = state[0]
        t.penup()
        t.goto(-150, 100)
        t.right(180)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300)
    if state[3] != "" and state[4] != "" and state[5] != "" and state[3] == state[4] == state[5]:
        winner = state[3]
        t.penup()
        t.goto(-150, 0)
        t.right(180)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300)
    if state[6] != "" and state[7] != "" and state[8] != "" and state[6] == state[7] == state[8]:
        winner = state[6]
        t.penup()
        t.goto(-150, -100)
        t.right(180)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300)
    if state[0] != "" and state[3] != "" and state[6] != "" and state[0] == state[3] == state[6]:
        winner = state[0]
        t.penup()
        t.goto(-100, 150)
        t.left(90)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300)
    if state[1] != "" and state[4] != "" and state[7] != "" and state[1] == state[4] == state[7]:
        winner = state[1]
        t.penup()
        t.goto(0, 150)
        t.left(90)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300)
    if state[2] != "" and state[5] != "" and state[8] != "" and state[2] == state[5] == state[8]:
        winner = state[2]
        t.penup()
        t.goto(100, 150)
        t.left(90)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300)
    if state[0] != "" and state[4] != "" and state[8] != "" and state[0] == state[4] == state[8]:
        winner = state[0]
        t.penup()
        t.goto(-150, 150)
        t.left(135)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300*(2**0.5))
    if state[2] != "" and state[4] != "" and state[6] != "" and state[2] == state[4] == state[6]:
        winner = state[2]
        t.penup()
        t.goto(150, 150)
        t.left(45)
        t.pendown()
        t.width("5")
        t.color("deep pink")
        t.forward(300 * (2 ** 0.5))
    if winner != "":
        t.penup()
        t.goto(0, 175)
        t.pendown()
        t.color("deep pink")
        style = ("Courier", 30, "bold")
        t.write(winner + ", YOU WON!", font = style, align = "center")
        t.penup()
        t.goto(-200, 200)
        time.sleep(4)
        s.bye()
    if turn > 9:
        t.penup()
        t.goto(0, 175)
        t.pendown()
        t.color("deep pink")
        style = ("Courier", 30, "bold")
        t.write("It's a DRAW!", font=style, align="center")
        t.penup()
        t.goto(-200, 200)
        time.sleep(3)
        s.bye()

s.mainloop()

