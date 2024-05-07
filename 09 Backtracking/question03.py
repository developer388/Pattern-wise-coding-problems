
def move(x, y, grid, counter, memo):
	
	key = str(x) + ',' + str(y)
	counter.append(key)
	
	if key in memo:
		return memo[key]

	if (x == 0) and (y == 0):
		return grid[x][y]

	if (x < 0) or (y < 0):
		return float('inf')

	up = grid[x][y] + move(x-1, y, grid, counter, memo)
	left = grid[x][y] + move(x, y-1, grid, counter, memo)

	memo[key] =  min(up, left)

	return memo[key]
	

def sol(grid):
	counter = []
	memo = {}
	ans = move(3,3, grid, counter, memo)
	print('ans:' ,ans, len(counter))


grid = [
    [1, 1, 1, 2],
    [2, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 2, 2, 1],    
]

sol(grid)


