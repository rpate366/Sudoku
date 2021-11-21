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

difficulty = "EASY"

#checking validity of entry
def validEntry(grid, row, col, val):
    #check row and col for recurrences
    for it in range(9):
        if grid[row][it]== val:
            return False
        if grid[it][col]== val:
            return False
    #check subgrid for recurrences
    it = row//3
    jt = col//3
    for row in range(it * 3, it * 3 + 3):
        for col in range (jt * 3, jt * 3 + 3):
            if grid[row][col]== val:
                return False
    return True

#adding Numbers to Board, called recursively
def addNum2Board(repetitions, t_grid):
    escape = False
    #only escape when a valid random number is generated
    while not escape:
        value = random.randint(0,8)
        row = random.randint(0,8)
        col = random.randint(0,8)

        escape = validEntry(t_grid, row, col, value)

    #add valid number to grid
    t_grid[row][col] = value

    #recursion
    if (repetitions - 1 == 0):
        return t_grid
    else:
        return addNum2Board(repetitions - 1, t_grid)

#creates board using addNum2Board()
def createBoard(difficulty):
    #determining how many numbers to start with on the board, based on difficulty
    #if only python had switch statements lol
    generate = int()
    if (difficulty == "RAND"):
        generate = random.randint(10,50)
    elif (difficulty == "MED"):
        generate = random.randint(21,30)
    elif (difficulty == "HARD"):
        generate = random.randint(13,18)
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

#initialize the grid depending on the difficulty
grid = createBoard(difficulty)

#system font
font1 = pygame.font.SysFont("timesnewroman",40)

#highlight selection
def draw_highlight():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * unit - 3, (y + i) * unit), (x * unit + unit + 3, (y + i) * unit), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i) * unit, y * unit ), ((x + i) * unit, y * unit + unit), 7)  

#draw grid
def draw():
    for row in range (9):
        for col in range (9):
            if grid[row][col]!= 0:
 
                # fill gray color in numbered slots
                pygame.draw.rect(screen, (128, 128, 128), (row * unit, col * unit, unit + 1, unit + 1))
 
                # init grid
                text1 = font1.render(str(grid[row][col]), 1, (0, 0, 0))
                screen.blit(text1, (row * unit + 28, col * unit + 22))

    # draw lines to make grid         
    for row in range(10):
        if row % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, row * unit), (s_width, row * unit), thick)
        pygame.draw.line(screen, (0, 0, 0), (row * unit, 0), (row * unit, s_width), thick)     

#solve grid using backtracking algorithm
def solve(grid, row, col):
    #check if box we are solving for needs solving
    while (grid[row][col] != 0):
        if row < 8:
            row+= 1
        elif row == 8 & col < 8:
            col += 1
            row = 0
        elif row == 8 & col ==8:
            return True

    #allow internal actions
    pygame.event.pump()

    #solve given box
    for val in range(1,10):
        if validEntry(grid, row, col, val) == 1:
            grid[row][col]= val
            global x, y
            x = row
            y = col

            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_highlight()
            pygame.display.update()
            pygame.time.delay(200)
            if solve(grid, row, col)== 1:
                return True
            else:
                grid[row][col]= 0
         
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_highlight()
            pygame.display.update()
            pygame.time.delay(200)

    return grid

#running the program
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve(grid, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()

pygame.quit()