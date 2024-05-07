# Check if a given string is palindrome using recursion.


def solution(string, firstIndex, lastIndex):

	if lastIndex == 0:
		return True

	return string[firstIndex] == string[lastIndex] and solution(string, firstIndex+1, lastIndex-1)
	



string = "LEVELL"
print("Result: ", solution(string, 0, len(string)-1))