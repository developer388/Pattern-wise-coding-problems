'''
Question: https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

'''

def isSafe(x, y, maze, visited):
    return (x > -1 and y > -1) and (x < len(maze) and y < len(maze)) and maze[x][y] == 1 and visited[x][y] == False


def move(x, y, maze, visited, path , answer):

    if (x==(len(maze)-1)) and (y==(len(maze)-1)):
        answer.append(path)
        return

    if isSafe(x, y, maze, visited):

        visited[x][y] = True
        # down
        path = path + 'D'
        move(x+1, y, maze, visited, path , answer)
        path = path[:-1]            # while backtracking remove the character from the result string
        # right
        path = path + 'R'
        move(x, y+1, maze, visited, path , answer)
        path = path[:-1]

        # left
        path = path + 'L'
        move(x, y-1, maze, visited, path , answer)
        path = path[:-1]

        # up
        path = path + 'U'
        move(x-1, y, maze, visited, path , answer)
        path = path[:-1]

        visited[x][y] = False      # while backtracking set the visited as false

def solution(maze):
    visited = []

    for i in range(4):
        visited.append([False, False, False, False])

    answer = []

    move(0, 0, maze, visited, '', answer)
    return answer



maze = [
[1, 0, 0, 0],
[1, 1, 0, 1],
[1, 1, 0, 0],
[0, 1, 1, 1]]



print('Answer: ', solution(maze))


