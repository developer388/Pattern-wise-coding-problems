# Print numbers from 1 to N using head recursion.


def solution(n):

	if n == 0:
		return

	solution(n-1)
	print(n)
	

solution(10)