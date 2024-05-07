'''
Given a rat maze represented by a 2D matrix, return all paths from source 0,0 to destination 3,3.

We can only move 'down' or 'right'.

'''

def isValid(x, y, maze):
    return ((x > -1) and (x < len(maze)) and (y > -1) and (y < len(maze)))

def move(x, y, maze, curr, ans):

    if (x == (len(maze) - 1)) and (y == (len(maze) - 1)):
        curr.append([x, y])
        ans.append(curr[:])
        curr.pop()
        return True

    if isValid(x, y, maze):     
        curr.append([x, y])

        # down
        move(x+1, y, maze, curr, ans)
        
        # right
        move(x, y+1, maze, curr, ans)
       
        curr.pop()
    
def solution(maze):
    ans = []
    curr = []

    move(1,1, maze, curr, ans)
    print('ANS:', ans, len(ans))

maze = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],    
]

solution(maze)