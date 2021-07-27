import pygame, keyboard, mouse

pygame.init()

run = True
pause = False
KOpposites = {"a": "d", "d": "a"}
clock = pygame.time.Clock()
atimer = 0
dtimer = 0
pausetimer = 0

while run:
    clock.tick(550)
    if not pause:
        if mouse.is_pressed("middle") and pausetimer == 0:
            pause = True
            pausetimer = 200
            print("PAUSED CHEATS")

        if keyboard.is_pressed("a"):
            if atimer < 130:
                atimer += 2

        if keyboard.is_pressed("d"):
            if dtimer < 130:
                dtimer += 2

        if keyboard.is_pressed("a") or keyboard.is_pressed("d"):
            pass

        else:
            if atimer > 0:
                keyboard.press("d")
                pygame.time.wait(atimer)
                keyboard.release("d")
                atimer = 0

            if dtimer > 0:
                keyboard.press("a")
                pygame.time.wait(dtimer)
                keyboard.release("a")
                dtimer = 0

    else:
        if mouse.is_pressed("middle") and pausetimer == 0:
            pause = False
            pausetimer = 200
            print("UNPAUSED CHEATS")

    if pausetimer > 0:
        pausetimer -= 1
