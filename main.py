#import needed libraries
from operator import add
import pygame
import random
import sys
from generateBoard import createBoard, validEntry

if __name__ == "__main__":

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
    x = 0
    y = 0
        #unit is how wide one box is
    unit = s_width / 9
        #val is the current value to be assigned
    val = 0

    difficulty = "MED"

    #initialize the grid depending on the difficulty
    grid = createBoard(difficulty= difficulty)

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

    def solve(grid, i, j):
        while grid[i][j]!= 0:
            if i<8:
                i+= 1
            elif i == 8 and j<8:
                i = 0
                j+= 1
            elif i == 8 and j == 8:
                return True

        pygame.event.pump()   

        for it in range(1, 10):
            if validEntry(grid, i, j, it)== True:
                grid[i][j]= it
                global x, y
                x = i
                y = j

                # reset graphics for advance
                screen.fill((255, 255, 255))
                draw()
                draw_highlight()
                pygame.display.update()

                if solve(grid, i, j)== 1:
                    return True
                else:
                    grid[i][j]= 0

                # reset graphics for backtrack
                screen.fill((255, 255, 255))
                draw()
                draw_highlight()
                pygame.display.update()   
                
        return False 

    #running the program
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if solve(grid, 0, 0) == True:
                        print("SOLVED")
                    else:
                        print("ERROR")

        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()

    pygame.quit()
    sys.quit()