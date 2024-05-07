# Print sum of N natural numbers using recursion. Example: Sum of numbers from 1 to 10 is 55. 

# Sum of ith number is ith number + sum(ith number-1) 

def solution(n):
	if n<2:
		return 1

	return n + solution(n-1)


print('Result: ', solution(10))