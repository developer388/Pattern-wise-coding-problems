# Print the nth fibonacci number.

def solution(number):
	if number <= 1:
		return number

	return solution(number-1) + solution(number-2)

print('Result: ', solution(6))