# Print numbers from N to 1 using tail recursion.


def solution(n):
	if n < 1:
		return

	print(n)
	solution(n-1)


solution(10)