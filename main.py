import pgzrun
import random
import pygame

pygame.mouse.set_visible(False)

WIDTH = 720
HEIGHT = 480

target1 = Actor('target_red1')
target2 = Actor('target_colored')
duck1 = Actor('duck_brown')
crosshair = Actor('crosshair_white_large')


score = 0



def update():
    target1.x += random.randint(2, 5)
    target2.x += random.randint(1, 3)
    duck1.x += 3
    if target1.left > WIDTH:
        target1.right = 0
        target1.top = random.randint(0, HEIGHT - target1.height)
    if target2.left > WIDTH:
        target2.right = 0
        target2.top = random.randint(0, HEIGHT - target2.height)
    if duck1.left > WIDTH:
        duck1.right = 0
        duck1.top = random.randint(0, HEIGHT - duck1.height)



def on_mouse_move(pos):
    #print(pos)
    crosshair.pos = pos

def on_mouse_down(pos):
    global score
    crosshair.pos = pos
    if crosshair.colliderect(target1):
        target1.right = 0
        target1.top = random.randint(0, HEIGHT - target1.height)
        score += 10
    elif crosshair.colliderect(target2):
        target2.right = 0
        target2.top = random.randint(0, HEIGHT - target2.height)
        score += 10
    elif crosshair.colliderect(duck1):
        duck1.right = 0
        duck1.top = random.randint(0, HEIGHT - duck1.height)
        score -= 50


def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    duck1.draw()
    crosshair.draw()
    screen.draw.text(str(score), (10,10),fontsize = 40)

pgzrun.go()