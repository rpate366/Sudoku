import random

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


def createBoard(difficulty):
    #determining how many numbers to start with on the board, based on difficulty
        #if only python had switch statements lol
        generate = int()
        if (difficulty == "EASY"):
            generate = random.randint(37,50)
        elif (difficulty == "MED"):
            generate = random.randint(21,30)
        elif (difficulty == "HARD"):
            generate = random.randint(13,18)
        else:
            generate = random.randint(10,50)

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