import pygame as pg
import numpy as np
import math

# pg setup
pg.init()
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
clock = pg.time.Clock()
running = True

WIDTH, HEIGHT = screen.get_size()

speed = 1
a1, a2, a3 = 0, 0, 0

def sin(angle):
    ra = math.sin(math.radians(angle))
    return ra

def cos(angle):
    ra = math.cos(math.radians(angle))
    return ra


dots = [np.array([1, 1, -1]), np.array([1, -1, -1]), np.array([1, -1, 1]), np.array([1, 1, 1]), np.array([-1, 1, -1]), np.array([-1, -1, -1]), np.array([-1, -1, 1]), np.array([-1, 1, 1])]


def applyRotation(pos):
    a = np.dot(xrot, pos)
    a = np.dot(yrot, a)
    a = np.dot(zrot, a)
    return a

def drawPoints(points, color=(255, 255, 255), multiplier=200, offsetx=0, offsety=0, size=8):
    for point in points:
        pg.draw.circle(screen, color, (point[0] * multiplier + offsetx, point[1] * 200 + offsety), size)


def drawPointsCentered(points, color=(255, 255, 255), multiplier=200, size=8):
    for point in points:
        point = applyRotation(point)
        pg.draw.circle(screen, color, (point[0] * multiplier + WIDTH / 2, point[1] * 200 + HEIGHT / 2), size)

#def drawLines(lines):
#    for line in lines:
#        pg.drawLine(screen, (255,255,255), (line[0], line[1]), (line[2], line[3]))

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # detect keys
    if pg.key.get_pressed()[pg.K_w] == True:
        a1 += speed
    if pg.key.get_pressed()[pg.K_s] == True:
        a1 -= speed
    if pg.key.get_pressed()[pg.K_d] == True:
        a2 += speed
    if pg.key.get_pressed()[pg.K_a] == True:
        a2 -= speed
    if pg.key.get_pressed()[pg.K_x] == True:
        a3 += speed
    if pg.key.get_pressed()[pg.K_z] == True:
        a3 -= speed

    # update variables
    xrot = np.array([[1, 0, 0],
        [0, cos(a1), sin(a1) * -1],
        [0, sin(a1), cos(a1)]])
    
    yrot = np.array([[cos(a2), 0, sin(a2)],
        [0, 1, 0],
        [sin(a2) * -1, 0, cos(a2)]])

    zrot = np.array([[cos(a3), sin(a3) * -1, 0],
        [sin(a3), cos(a3), 0],
        [0, 0, 1]])

    WIDTH, HEIGHT = screen.get_size()
    a1 += 1
    a2 += 1
    a3 += 1
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pg.Color(0,0,0))

    # RENDER YOUR GAME HERE
    points = drawPointsCentered(dots)
    #line1 = pg.draw.line(screen, (255,0,0), (d1pa[0] * 200 + WIDTH / 2, d1pa[1] * 200 + HEIGHT / 2), (d2pa[0] * 200 + WIDTH / 2, d2pa[1] * 200 + HEIGHT / 2))
    #line2 = pg.draw.line(screen, (0,255,0), (d1pa[0] * 200 + WIDTH / 2, d1pa[1] * 200 + HEIGHT / 2), (d5pa[0] * 200 + WIDTH / 2, d5pa[1] * 200 + HEIGHT / 2))
    #line3 = pg.draw.line(screen, (0,0,255), (d1pa[0] * 200 + WIDTH / 2, d1pa[1] * 200 + HEIGHT / 2), (d4pa[0] * 200 + WIDTH / 2, d4pa[1] * 200 + HEIGHT / 2))
    #line4 = pg.draw.line(screen, (255,255,255), (d2pa[0] * 200 + WIDTH / 2, d2pa[1] * 200 + HEIGHT / 2), (d3pa[0] * 200 + WIDTH / 2, d3pa[1] * 200 + HEIGHT / 2))
    #line5 = pg.draw.line(screen, (255,255,255), (d2pa[0] * 200 + WIDTH / 2, d2pa[1] * 200 + HEIGHT / 2), (d6pa[0] * 200 + WIDTH / 2, d6pa[1] * 200 + HEIGHT / 2))
    #line6 = pg.draw.line(screen, (255,255,255), (d5pa[0] * 200 + WIDTH / 2, d5pa[1] * 200 + HEIGHT / 2), (d6pa[0] * 200 + WIDTH / 2, d6pa[1] * 200 + HEIGHT / 2))
    #line7 = pg.draw.line(screen, (255,255,255), (d3pa[0] * 200 + WIDTH / 2, d3pa[1] * 200 + HEIGHT / 2), (d4pa[0] * 200 + WIDTH / 2, d4pa[1] * 200 + HEIGHT / 2))
    #line8 = pg.draw.line(screen, (255,255,255), (d4pa[0] * 200 + WIDTH / 2, d4pa[1] * 200 + HEIGHT / 2), (d8pa[0] * 200 + WIDTH / 2, d8pa[1] * 200 + HEIGHT / 2))
    #line9 = pg.draw.line(screen, (255,255,255), (d3pa[0] * 200 + WIDTH / 2, d3pa[1] * 200 + HEIGHT / 2), (d7pa[0] * 200 + WIDTH / 2, d7pa[1] * 200 + HEIGHT / 2))
    #line10 = pg.draw.line(screen, (255,255,255), (d5pa[0] * 200 + WIDTH / 2, d5pa[1] * 200 + HEIGHT / 2), (d8pa[0] * 200 + WIDTH / 2, d8pa[1] * 200 + HEIGHT / 2))
    #line11 = pg.draw.line(screen, (255,255,255), (d6pa[0] * 200 + WIDTH / 2, d6pa[1] * 200 + HEIGHT / 2), (d7pa[0] * 200 + WIDTH / 2, d7pa[1] * 200 + HEIGHT / 2))
    #line12 = pg.draw.line(screen, (255,255,255), (d7pa[0] * 200 + WIDTH / 2, d7pa[1] * 200 + HEIGHT / 2), (d8pa[0] * 200 + WIDTH / 2, d8pa[1] * 200 + HEIGHT / 2))
    #print(d1pa)
    
    
    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()
