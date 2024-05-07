# Question 1: Print numbers from 1 to N using tail recursion.

def solution(i, n):

	if i>n:
		return

	print(i)
	solution(i+1, n)


solution(1, 10)