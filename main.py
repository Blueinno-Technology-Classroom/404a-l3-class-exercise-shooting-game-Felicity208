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
scoring1 = Actor('text_plus')
scoring2 = Actor('text_1')
scoring3 = Actor('text_0')
scoring1.y = 530
scoring1.x = 600
scoring2.y = 530
scoring2.x = 640
scoring3.y = 530
scoring3.x = 680

score = 0
hit = False


def update():
    global hit
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
    
    if hit:
        scoring1.y -= 6
        scoring2.y -= 6
        scoring3.y -= 6
        if scoring1.y < 400:
            hit = False
            scoring1.y = 530
            scoring2.y = 530
            scoring3.y = 530

def on_mouse_move(pos):
    #print(pos)
    crosshair.pos = pos

def on_mouse_down(pos):
    global score, hit
    music.play_once('pop')
    crosshair.pos = pos
    if crosshair.colliderect(target1):
        target1.right = 0
        target1.top = random.randint(0, HEIGHT - target1.height)
        score += 10
        hit = True
        scoring1.y = 530
        scoring2.y = 530
        scoring3.y = 530
    elif crosshair.colliderect(target2):
        target2.right = 0
        target2.top = random.randint(0, HEIGHT - target2.height)
        score += 10
        hit = True
        scoring1.y = 530
        scoring2.y = 530
        scoring3.y = 530
    elif crosshair.colliderect(duck1):
        duck1.right = 0
        duck1.top = random.randint(0, HEIGHT - duck1.height)
        score -= 50
        music.play_once('duck')


def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    duck1.draw()
    scoring1.draw()
    scoring2.draw()
    scoring3.draw()
    crosshair.draw()
    screen.draw.text(str(score), (10,10),fontsize = 40)

pgzrun.go()