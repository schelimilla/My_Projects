import gamebox
import pygame
import random

camera = gamebox.Camera(800, 600)

player_box = gamebox.from_color(50,275,"red", 25, 25)
player_box.yspeed = 0
ground_box = gamebox.from_color(400,600,"green", 1000000, 50)
ceiling_box = gamebox.from_color(400,0,"light blue", 1000000, 50)
flappybird_sheet = gamebox.load_sprite_sheet('flappybird.png',1,1)
flappybird_box = gamebox.from_image(50, 275, flappybird_sheet[0])
player_box = flappybird_box
player_box.scale_by(0.2)
fbbg_sheet = gamebox.load_sprite_sheet('fbbg.png',1,1)
fbbg = gamebox.from_image(50, 275, fbbg_sheet[0])
fbbg.scale_by(0.75)


camera.draw("Flappy Bird", 100, "gold", 400, 100)

camera.display()

game_on = False



counter = 0
n = 200
z = 600
walls = []
score = 0
xy_list = []


def tick(keys):
    global game_on
    global player_box
    global counter
    global n
    global z
    global walls
    global score
    global xy_list

    if game_on == True:

        camera.clear("white")
        camera.draw(fbbg)
        player_box.speedy += 2
        player_box.move_speed()
        player_box.move_to_stop_overlapping(ground_box)


        if player_box.bottom_touches(ground_box):
            player_box.speedy = 0
            game_on = False
            camera.draw("DEAD", 100, "red", 400, 100)

        if pygame.K_SPACE in keys:
            player_box.speedy = -13

        if pygame.K_SPACE in keys:
            player_box.yspeed += 0.25

        counter += 1
        if counter % 50 == 0:
            bottom_wall = gamebox.from_color(random.randint(n, z), camera.x + 175, "lawngreen", 50, random.randint(200, 500))
            n = bottom_wall.center[0]
            xpos = bottom_wall.center[0]
            if n > z - 50:
                z = n + 200
            top_wall = gamebox.from_color(xpos,camera.x - 400,"lawngreen",50,random.randint(200,400))

            walls.append(bottom_wall)
            walls.append(top_wall)
        for wall in walls:
            wall.x -= 3
            player_box.move_to_stop_overlapping(wall)
            camera.draw(wall)
            wall = str(wall)
            # print(wall)
            xy = wall[28:len(wall) + 1]
            xy_list.append(xy)
            # print(xy_list)
            last = xy_list[-1]
            # print(last)
            comma = last.find(',')
            xp = last[0:comma]
            xp = int(xp)
            if player_box.center[0] > xp:
                score += 1
            score_display = gamebox.from_text(40, 50, str(score), 50, "pink")
            # camera.draw(score_display)

        camera.draw(player_box)
        # camera.draw(ground_box)

        for wall in walls:
            if player_box.touches(wall):
                player_box.speedy = 0
                game_on = False
                camera.draw("DEAD", 100, "red", 400, 100)

        camera.display()

    else:
        if pygame.K_SPACE in keys:
            game_on = True
            walls = []
            counter = 0
            n = 200
            z = 600
            xy_list = []
            score = 0

ticks_per_second = 40
gamebox.timer_loop(ticks_per_second, tick)