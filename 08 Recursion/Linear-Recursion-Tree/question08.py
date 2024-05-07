# Reverse a given string using using recursion.


def solution(string, lastIndex):

	if lastIndex == 0:
		return string[lastIndex]

	return string[lastIndex] + solution(string, lastIndex-1)



s = ["N","I","K","H","I","L"]

print('Result: ', solution(s, len(s)-1))
