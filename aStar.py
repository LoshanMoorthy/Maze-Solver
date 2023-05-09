from pyamaze import maze, agent
from queue import PriorityQueue

'Creating the heuristic function for A* algorithm'
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    'Output is the manhattan distance between to two cells'
    return abs(x1 - x2) + abs(y1 - y2)

'Function for A* algorithm (input is one maze)'
def aStar(m):
    'Defining the start cell which is the last row, and column'
    start = (m.rows, m.cols)
    'Dictionary comprehension for G score and F score'
    g_Score = {cell:float('inf') for cell in m.grid}
    'G score value for the start cell is 0'
    g_Score[start] = 0

    f_Score = {cell:float('inf') for cell in m.grid}
    'F scores start cell is the manhattan distance between the start cell and goal cell'
    f_Score[start] = h(start, (1, 1))

    open = PriorityQueue()
    open.put((h(start, (1, 1)), h(start, (1, 1)), start))
    'a path is the reverse path'
    aPath = {}

    while not open.empty():
        'Current cell has the minimum value on the basis of the F course and the basis of F course'
        currentCell = open.get()[2]
        'If goal cell is met, we will break'
        if currentCell == (1, 1):
            break
        'Iterates through all neighbours - East, South, North and West'
        for d in 'ESNW':
            'Checks if path is equal to 1, which means path is open'
            if m.maze_map[currentCell][d] == True:
                if d == 'E':
                    childCell = (currentCell[0], currentCell[1] + 1)
                if d == 'W':
                    childCell = (currentCell[0], currentCell[1] - 1)
                if d == 'N':
                    childCell = (currentCell[0] - 1, currentCell[1])
                if d == 'S':
                    childCell = (currentCell[0] + 1, currentCell[1])

                'Once child is found we calculate a new G score'
                tempGScore = g_Score[currentCell] + 1
                tempFScore = tempGScore + h(childCell, (1, 1))

                'We check if new F score is less than previous F Score'
                if tempFScore < f_Score[childCell]:
                    'If true we update G score and F score of child cell'
                    g_Score[childCell] = tempGScore
                    f_Score[childCell] = tempFScore
                    'We add one entry into the PriorityQueue'
                    open.put((tempFScore, h(childCell, (1, 1)), childCell))
                    'Adding one key value child cell, and the value as current cell' 
                    aPath[childCell] = currentCell  
    fwdPath = {}
    'The path from goal to start cell, i will go through the values in the a path dict'
    cell = (1, 1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath    

m = maze(5, 5)
m.CreateMaze()
path = aStar(m)

a = agent(m, footprints = True)
m.tracePath({a:path})

m.run()