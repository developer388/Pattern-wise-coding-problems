# Calculate factorial of a given number using recursion.


def solution(n):
	if n == 1:
		return 1

	return n * solution(n-1)




print('Result:', solution(3))