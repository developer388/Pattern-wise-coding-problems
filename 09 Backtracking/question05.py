'''
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.
0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:
 Starting at the position (0, 0) and reaching (n-1, n 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n-1, n 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n-1, n = 1), then no cherries can be collected.

Example 1
Input: grid = [[0, 1, -1], [1, 0, -1], [1,1,1]] Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2). 4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1], [0,0,-1), [0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry. The total number of cherries picked up is 5, and this is the maximum possible.
'''

def isSafe(x, y, grid, visited):
	return ((x > -1) and (x < len(grid))) and ((y > -1) and (y < len(grid))) and (grid[x][y] != -1) and (visited[x][y] == False)

def move1(x, y, grid, visited, counter):
	
	if (x == (len(grid)-1)) and (y == (len(grid)-1)):		
		print(f'grid[{x}][{y}]={grid[x][y]} visited[{x}][{y}]={visited[x][y]}')
		if grid[x][y] == 1:
			counter[0] = counter[0] + 1
			grid[x][y] = 0
		visited[x][y] = True
		return 

	if isSafe(x,y, grid, visited):

		print(f'grid[{x}][{y}]={grid[x][y]} visited[{x}][{y}]={visited[x][y]}')

		if grid[x][y] == 1:
			counter[0] = counter[0] + 1
			grid[x][y] = 0

		visited[x][y] = True
		move1(x+1, y, grid, visited, counter)
		move1(x, y+1, grid, visited, counter)



def solution(grid):
   counter = [0]
   visited = []
   for i in range(3):
   		visited.append([False, False, False])

   move1(0, 0, grid, visited, counter)

   print('Result: ', counter[0])


grid = [[0, 1, -1], [1, 0, -1], [1,1,1]]

solution(grid)
