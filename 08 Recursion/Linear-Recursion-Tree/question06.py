# Calculate power of x to the y using recursion.

def solution(x, y):
	if y == 0:
		return 1
	return x * solution(x, y-1)


print('Result: ', solution(2, 5))