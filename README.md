# Maze-Solver

## Maze World - Pyamaze

A simple A-Star/A* algorithm used to solve a Maze. 

### Boring theory

Unlike Breadth-first search and Depth-first search which are 'uninformed' blind searched A* search is an ***informed*** search algorithm. This basically means that it will take into account the 
location of the goal while deciding the next move. So, the algorithm finds the shortest path between two nodes taking into account both the cost of reaching a node (g-score) and the estimated 
cost to the goal from that node (h-score).

### Code explanation

1. Initialization:

- The algorithm takes a maze object 'm' as input.
- It defines the start cell, which is the last row and column of the maze.
- Two dictionaries, 'g_Score' and 'f_Score', are created to store the g-score and f-score values for each cell in the maze. The initial values are set to infinity except for the start cell.
- A priority queue 'open' is created to store cells based on their f-score.

2. Heuristic Function:

- The provided code defines the heuristic function 'h(cell1, cell2)' that calculates the Manhattan distance between two cells. 
  The Manhattan distance is the sum of the absolute differences of their x and y coordinates.

2. A* Algorithm Loop:

- The algorithm enters a loop until the 'open' priority queue is empty.
- In each iteration, the algorithm selects the cell with the minimum f-score from the 'open' queue as the current cell.
- If the current cell is the goal cell (cell (1, 1)), the algorithm breaks out of the loop as the goal has been reached.
- For each neighboring cell (east, south, north, west) of the current cell:
   - If the path to the neighbor is open (value is True in the maze_map), the algorithm proceeds.
   - The child cell is determined based on the direction.
   - The algorithm calculates a new g-score for the child cell by adding 1 to the g-score of the current cell.
   - The algorithm calculates a new f-score for the child cell by adding the new g-score and the heuristic value h(childCell, (1, 1)).
   - If the new f-score is lower than the previous f-score of the child cell, it means a better path has been found. The g-score and f-score of the child cell are updated, and the child cell is added to the 'open' queue.
   - The 'aPath' dictionary is updated to store the current cell as the parent of the child cell.

2. Trace Path:

- Once the goal cell has been reached, the algorithm reconstructs the path from the start cell to the goal cell.
- The 'fwdPath' dictionary is used to store the forward path, starting from the goal cell and going back to the start cell, using the 'aPath' dictionary.
- The start cell is (m.rows, m.cols), and the algorithm iteratively follows the parent cells stored in 'aPath' until it reaches the start cell.
