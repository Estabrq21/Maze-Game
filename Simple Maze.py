import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

# initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000), pygame.DOUBLEBUF|pygame.OPENGL)
pygame.display.set_caption('Maze')

# set up OpenGL
glViewport(0, 0, 1000, 1000)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0, 1000, 1000, 0)
glMatrixMode(GL_MODELVIEW)

# create maze
maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1],
        [1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1],
        [1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1],
        [1,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1],
        [1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,0,0,0,1],
        [1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

# set up player
player_x = 1
player_y = 1

# set up clock
clock = pygame.time.Clock()

# main game loop
while True:
# handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if maze[player_y][player_x-1] == 0:
            player_x -= 1
    if keys[pygame.K_RIGHT]:
        if maze[player_y][player_x+1] == 0:
            player_x += 1
    if keys[pygame.K_UP]:
        if maze[player_y-1][player_x] == 0:
            player_y -= 1
    if keys[pygame.K_DOWN]:
        if maze[player_y+1][player_x] == 0:
            player_y += 1

    # clear screen
    glClear(GL_COLOR_BUFFER_BIT)

    # draw maze
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                glColor3f(1,1 ,1 )
            else:
                glColor3f(0, 0, 0)
            glBegin(GL_QUADS)
            glVertex2f(x*50, y*50)
            glVertex2f(x*50+50, y*50)
            glVertex2f(x*50+50, y*50+50)
            glVertex2f(x*50, y*50+50)
            glEnd()

    # draw player
    glColor3f(189, 0, 235)
    glBegin(GL_QUADS)
    glVertex2f(player_x*50+10, player_y*50+10)
    glVertex2f(player_x*50+40, player_y*50+10)
    glVertex2f(player_x*50+40, player_y*50+40)
    glVertex2f(player_x*50+10, player_y*50+40)
    glEnd()

    # update screen
    pygame.display.flip()

    # regulate frame rate
    clock.tick(8)