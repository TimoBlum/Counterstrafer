import pygame, keyboard, mouse

pygame.init()

run = True
pause = False
clock = pygame.time.Clock()
atimer = 0
dtimer = 0
pausetimer = 0
layout = input("Is your keyboard layout QWERTY (0) or AZERTY (1)? ")
if int(layout) == 0:
    left = "a"
    right = "d"
elif int(layout) == 1:
    left = "q"
    right = "d"

while run:
    clock.tick(550)
    if not pause:
        if mouse.is_pressed("middle") and pausetimer == 0:
            pause = True
            pausetimer = 200
            print("PAUSED CHEATS")

        if keyboard.is_pressed(left):
            if atimer < 130:
                atimer += 2

        if keyboard.is_pressed(right):
            if dtimer < 130:
                dtimer += 2

        if keyboard.is_pressed(left) or keyboard.is_pressed(right):
            pass

        else:
            if atimer > 0:
                keyboard.press(right)
                pygame.time.wait(atimer)
                keyboard.release(right)
                atimer = 0

            if dtimer > 0:
                keyboard.press(left)
                pygame.time.wait(dtimer)
                keyboard.release(left)
                dtimer = 0

    else:
        if mouse.is_pressed("middle") and pausetimer == 0:
            pause = False
            pausetimer = 200
            print("UNPAUSED CHEATS")

    if pausetimer > 0:
        pausetimer -= 1
