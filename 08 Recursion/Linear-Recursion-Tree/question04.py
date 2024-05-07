# Print numbers from N to 1 using head recursion.


def solution(i, n):
	if i > n:
		return

	solution(i+1, n)
	print(i)
	


solution(1, 10)