# Print sum of digits of a number using recursion.

import math

def solution(n):

	print(f'n={n}')
	if n==0:
		return 0

	return n%10 + solution(math.floor(n/10))


print('Result: ', solution(11011))








# def iterativeSolution(number):

# 	divider = 1

# 	result = 0

# 	while 






# print('Result using iterative solution: ', iterativeSolution(1524))