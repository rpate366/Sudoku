#import needed libraries
from operator import add
import pygame
import random

#int font, window, icon, and title
pygame.font.init()
s_width = 700
s_height = 800
screen = pygame.display.set_mode((s_width, s_height)) 
screen.fill((255, 255, 255))
icon = pygame.image.load('icon_v.jpeg')
pygame.display.set_icon(icon)
pygame.display.set_caption("SUDOKU USING BACKTRACKING")

#declaring var to setup board
    #x and y are coords
x = 7
y = 2
    #unit is how wide one box is
unit = s_width / 9
    #val is the current value to be assigned
val = 0

difficulty = "HARD"

#checking validity of entry
def validEntry(m, i, j, val):
    for it in range(9):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== val:
                return False
    return True

#adding Numbers to Board, called recursively
def addNum2Board(repetitions, t_grid):
    escape = False
    while not escape:
        value = random.randint(0,8)
        row = random.randint(0,8)
        col = random.randint(0,8)

        escape = validEntry(t_grid, row, col, value)

    t_grid[row][col] = value

    if (repetitions - 1 == 0):
        return t_grid
    else:
        return addNum2Board(repetitions - 1, t_grid)

#creates board using addNum2Board()
def createBoard(difficulty):
    #determining how many numbers to start with on the board, based on difficulty
    #if only python had switch statements lol
    generate = 0
    if (difficulty == "HARD"):
        generate = random.randint(13,18)
    elif (difficulty == "MED"):
        generate = random.randint(21,30)
    else:
        generate = random.randint(37,50)

    default =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    return addNum2Board(generate, default)

#using default board for now, creating an initializing function later
grid = createBoard(difficulty)

font1 = pygame.font.SysFont("timesnewroman",40)

def draw_highlight():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * unit - 3, (y + i) * unit), (x * unit + unit + 3, (y + i) * unit), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i) * unit, y * unit ), ((x + i) * unit, y * unit + unit), 7)  

def draw():
    for row in range (9):
        for col in range (9):
            if grid[row][col]!= 0:
 
                # fill gray color in numbered slots
                pygame.draw.rect(screen, (128, 128, 128), (row * unit, col * unit, unit + 1, unit + 1))
 
                # init grid
                text1 = font1.render(str(grid[row][col]), 1, (200, 0, 0))
                screen.blit(text1, (row * unit + 28, col * unit + 22))

    # draw lines to make grid         
    for row in range(10):
        if row % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, row * unit), (s_width, row * unit), thick)
        pygame.draw.line(screen, (0, 0, 0), (row * unit, 0), (row * unit, s_width), thick)     
 
#running the program
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()

pygame.quit()