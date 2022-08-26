import gamebox
import pygame
import random

camera = gamebox.Camera(800, 600)

timer = 0

background_sheet = gamebox.load_sprite_sheet('mountains.png',1,1)
mount_back = gamebox.from_image(400,300,background_sheet[0])
# mount_back.scale_by(0.3)


sheet = gamebox.load_sprite_sheet('plane.png',1,1)
rocket = gamebox.from_image(0, 200, sheet[0])
rocket.flip()
rocket.scale_by(0.15)

sheet2 = gamebox.load_sprite_sheet('plane.png',1,1)
rocket2 = gamebox.from_image(810, 500, sheet2[0])
rocket2.flip()
rocket2.scale_by(0.15)

sheet3 = gamebox.load_sprite_sheet('plane.png',1,1)
rocket3 = gamebox.from_image(810, 500, sheet3[0])
rocket3.flip()
rocket3.scale_by(0.15)

devil_emoji_sheet = gamebox.load_sprite_sheet('devil_emoji.png',1,1)
badguy = gamebox.from_image(300,275,devil_emoji_sheet[0])
badguy.scale_by(0.07)


player_box = gamebox.from_color(50,275,"blue", 25, 25)
# cool_emoji_sheet = gamebox.load_sprite_sheet('cool_emoji.png',1,1)
# player_box = gamebox.from_image(50,275,cool_emoji_sheet[0])
# player_box.scale_by(0.1)

cool_emoji_sheet = gamebox.load_sprite_sheet('cool_emoji.png',1,1)
cool_box = gamebox.from_image(50, 275, cool_emoji_sheet[0])
cool_box.scale_by(0.1)

nerd_emoji_sheet = gamebox.load_sprite_sheet('nerd_emoji.png',1,1)
nerd_box = gamebox.from_image(50, 275, nerd_emoji_sheet[0])
nerd_box.scale_by(0.1)

laughcry_emoji_sheet = gamebox.load_sprite_sheet('laughcry_emoji.png',1,1)
laughcry_box = gamebox.from_image(50, 275, laughcry_emoji_sheet[0])
laughcry_box.scale_by(0.07)

wink_emoji_sheet = gamebox.load_sprite_sheet('wink_emoji.png',1,1)
wink_box = gamebox.from_image(50, 275, wink_emoji_sheet[0])
wink_box.scale_by(0.1)

hearteyes_emoji_sheet = gamebox.load_sprite_sheet('hearteyes_emoji.png',1,1)
hearteyes_box = gamebox.from_image(50, 275, hearteyes_emoji_sheet[0])
hearteyes_box.scale_by(0.07)

player_box.yspeed = 0
ground_box = gamebox.from_color(400,600,"white", 1000000, 50)
ceiling_box = gamebox.from_color(400,0,"light blue", 1000000, 50)

coins = []
spritebox_list = []
score = 0

counter = 0
# rocket_counter = 0
n = 200
z = 600
m = 200
y = 600
walls = []
rocket_counter = 0
rocket_list = []
vblocks_counter = 0
vblocks_list = []
current_health = 200
xy_list = []
badguy_counter = 0

first_wall = gamebox.from_color(50, 300, "pink", 200, 30)

game_on = False

camera.draw("Sky Fly", 100, "blue", 400, 100)
camera.draw("Srini Chelimilla - slc8kf", 25, "magenta", 400, 150)
camera.draw("Press the up arrow to jump & press the left and right arrows to move horizontally", 30, "gold", 400, 200)
camera.draw("Jump on each moving block to collect a coin.", 30, "gold", 400, 250)
camera.draw("It's okay if you fall on the ground, but watch out, the devil will try to catch you!", 30, "gold", 400, 300)
camera.draw("If it touches you, your health decreases.", 30, "gold", 400, 350)
camera.draw("The longer you stay alive, the harder the game will get.", 30, "gold", 400, 400)
camera.draw("After certain amounts of time, there will be airplanes that are flying next you.", 30, "gold", 400, 450)
camera.draw("If it touches you, your health decreases.", 30, "gold", 400, 500)
camera.draw("Once you die, to start again, press the space bar!", 30, "gold", 400, 550)
camera.draw("Let's Begin! Press '0' to continue", 20, "orange", 400, 580)


camera.display()

def tick(keys):
    global game_on
    global walls
    global player_box
    global ground_box
    global counter
    global n
    global z
    global rocket
    global rocket2
    global rocket3
    global rocket_counter
    global rocket_list
    global vblocks_counter
    global vblocks_list
    global m
    global y
    global current_health
    global xy_list
    global coins
    global spritebox_list
    global score
    global mount_back
    # global sweat_box
    # global dead_box
    global laughcry_box
    global wink_box
    global hearteyes_box
    global cool_box
    global nerd_box
    global badguy
    global badguy_counter
    global timer

    if game_on == True:



        if pygame.K_RIGHT in keys:
            player_box.x += 10
        if pygame.K_LEFT in keys:
            player_box.x -= 10

        player_box.yspeed += 1
        player_box.y = player_box.y + player_box.yspeed

        camera.clear("white")
        # camera.x += 3



        camera.draw(mount_back)



        health_bar = gamebox.from_color(400, 50, "red", current_health * 2, 30)
        camera.draw(health_bar)


        for wall in walls:
            wall.x -= 5
            player_box.move_to_stop_overlapping(wall)
            camera.draw(wall)
            if player_box.bottom_touches(wall):
                player_box.yspeed = 0
                if pygame.K_UP in keys:
                    player_box.yspeed = -15



        if player_box.bottom_touches(ground_box):
            player_box.yspeed = 0
            if pygame.K_UP in keys:
                player_box.yspeed = -15


        counter += 1
        if counter % 50 == 0:
            new_wall = gamebox.from_color(random.randint(n,z), random.randint(350,550 ), "pink", random.randint(150, 200), 30)
            n = new_wall.center[0]
            # n = str(n)
            # print(n)
            if n > z - 50:
                z = n + 200
            walls.append(new_wall)
            # print(walls)

        for wall in walls:
            wall = str(wall)
            # print(wall)
            x = wall.find('x')
            space = wall.find(' ')
            spritebox = wall[0:x]+wall[x+1:space]
            if spritebox not in spritebox_list:
                spritebox_list.append(spritebox)
            # print(spritebox_list)
                xy = wall[28:len(wall)+1]
                xy_list.append(xy)
                # print(xy_list)
                last = xy_list[-1]
                # print(last)
                comma = last.find(',')
                xp = last[0:comma]
                xp = int(xp)
                yp = last[comma+1:len(last)+1]
                yp = int(yp)
            # print(type(xp))
            # print(yp)
                new_coin = gamebox.from_color(xp,yp - 30,"yellow",12,12)
                coins.append(new_coin)
        # print(xy_list)

        for coin in coins:
            coin.x -= 5
            if player_box.touches(coin):
                score += 100
                coins.remove(coin)
            camera.draw(coin)

        timer += 1 / 33
        timer_display = gamebox.from_text(750, 60, str(int(timer)), 30, "blue")
        camera.draw(timer_display)

        if timer >= 15:
            rocket.move_speed()
            rocket.x += 10
            camera.draw(rocket)
            # print(rocket.center[0])
            xpos = rocket.center[0]
            xpos = int(xpos)
            if xpos > random.randint(1000,1500):
                rocket.center = [0, 200]
            if rocket.touches(player_box):
                current_health -= 1
                if current_health <= 0:
                    camera.draw(gamebox.from_text(400, 300, "DEAD", 100, "red"))
                    camera.draw(gamebox.from_text(400, 350, "Your score is: " + str(score), 50, "purple"))
                    game_on = False

        if timer >= 60:
            rocket2.move_speed()
            rocket2.x += 10
            camera.draw(rocket2)
            # print(rocket.center[0])
            xpos2 = rocket2.center[0]
            xpos2 = int(xpos2)
            if xpos2 > random.randint(2000,2500):
                rocket2.center = [0, 450]
            if rocket2.touches(player_box):
                current_health -= 1
                if current_health <= 0:
                    camera.draw(gamebox.from_text(400, 300, "DEAD", 100, "red"))
                    camera.draw(gamebox.from_text(400, 350, "Your score is: " + str(score), 50, "purple"))
                    game_on = False

        if timer >= 120:
            rocket3.move_speed()
            rocket3.x += 10
            camera.draw(rocket3)
            # print(rocket.center[0])
            xpos3 = rocket3.center[0]
            xpos3 = int(xpos3)
            if xpos3 > random.randint(3000,3500):
                rocket3.center = [0, 350]
            if rocket3.touches(player_box):
                current_health -= 1
                if current_health <= 0:
                    camera.draw(gamebox.from_text(400, 300, "DEAD", 100, "red"))
                    camera.draw(gamebox.from_text(400, 350, "Your score is: " + str(score), 50, "purple"))
                    game_on = False


        badguy.move_to_stop_overlapping(ground_box)
        badguy.yspeed += 1
        badguy.y += badguy.yspeed
        if player_box.x < badguy.x:
            badguy.x -= 5
        if player_box.x > badguy.x:
            badguy.x += 5
        if badguy.touches(player_box):
            current_health -= 1
            if current_health <= 0:
                camera.draw(gamebox.from_text(400, 300, "DEAD", 100, "red"))
                camera.draw(gamebox.from_text(400, 350, "Your score is: " + str(score), 50, "purple"))
                game_on = False

        badguy_counter += 1
        if badguy_counter%300 == 0:
            badguy.yspeed = -15




        first_wall.x -= 5

        player_box.move_speed()
        player_box.move_to_stop_overlapping(ground_box)

        score_display = gamebox.from_text(40, 50, str(score), 50, "pink")
        camera.draw(score_display)

        if player_box.center[0] < -20:
            camera.draw(gamebox.from_text(400, 300, "DEAD", 100, "red"))
            camera.draw(gamebox.from_text(400, 350, "Your score is: " + str(score), 50, "purple"))
            game_on = False

        if player_box.center[0] > 820:
            camera.draw(gamebox.from_text(400, 300, "DEAD", 100, "red"))
            camera.draw(gamebox.from_text(400, 350, "Your score is: " + str(score), 50, "purple"))
            game_on = False



        camera.draw(player_box)
        camera.draw(ground_box)
        camera.draw(ceiling_box)
        camera.draw(first_wall)

        camera.draw(badguy)


        camera.display()

    elif pygame.K_c in keys:
        player_box = cool_box
        walls = []
        coins = []
        spritebox_list = []
        counter = 0
        n = 200
        z = 600
        score = 0
        current_health = 200
        timer = 0
        game_on = True



    elif pygame.K_n in keys:
        player_box = nerd_box
        # sweat_box.scale_by(0.1)
        game_on = True
        # player_box = gamebox.from_image(50, 275, cool_emoji_sheet[0])
        player_box = player_box
        # player_box.scale_by(0.1)
        walls = []
        coins = []
        spritebox_list = []
        counter = 0
        n = 200
        z = 600
        score = 0
        current_health = 200
        timer = 0

    elif pygame.K_j in keys:
        player_box = laughcry_box
        # sweat_box.scale_by(0.1)
        game_on = True
        # player_box = gamebox.from_image(50, 275, cool_emoji_sheet[0])
        player_box = player_box
        # player_box.scale_by(0.1)
        walls = []
        coins = []
        spritebox_list = []
        counter = 0
        n = 200
        z = 600
        score = 0
        current_health = 200
        timer = 0

    elif pygame.K_w in keys:
        player_box = wink_box
        # sweat_box.scale_by(0.1)
        game_on = True
        # player_box = gamebox.from_image(50, 275, cool_emoji_sheet[0])
        player_box = player_box
        # player_box.scale_by(0.1)
        walls = []
        coins = []
        spritebox_list = []
        counter = 0
        n = 200
        z = 600
        score = 0
        current_health = 200
        timer = 0

    elif pygame.K_h in keys:
        player_box = hearteyes_box
        # sweat_box.scale_by(0.1)
        game_on = True
        # player_box = gamebox.from_image(50, 275, cool_emoji_sheet[0])
        player_box = player_box
        # player_box.scale_by(0.1)
        walls = []
        coins = []
        spritebox_list = []
        counter = 0
        n = 200
        z = 600
        score = 0
        current_health = 200
        timer = 0

    elif pygame.K_SPACE in keys:
        walls = []
        coins = []
        spritebox_list = []
        counter = 0
        n = 200
        z = 600
        score = 0
        current_health = 200
        player_box.center = [50,300]
        game_on = True
        timer = 0

    elif pygame.K_0 in keys:
        camera.clear('black')
        camera.draw("Choose an emoji as your player!", 50, "magenta", 400, 200)
        camera.draw("Press 'c' to choose the emoji with sunglasses", 30, "gold", 400, 300)
        camera.draw("Press 'h' to choose the emoji with heart eyes", 30, "gold", 400, 350)
        camera.draw("Press 'j' to choose the emoji with tears of joy", 30, "gold", 400, 400)
        camera.draw("Press 'n' to choose the nerd emoji", 30, "gold", 400, 450)
        camera.draw("Press 'w' to choose the emoji with a winking face", 30, "gold", 400, 500)
        camera.display()




ticks_per_second = 45
gamebox.timer_loop(ticks_per_second, tick)








