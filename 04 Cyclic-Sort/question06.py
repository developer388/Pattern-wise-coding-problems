'''
We are given an unsorted array containing ‘n’ numbers taken from the range
1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’,
but due to a data error, one of the numbers got duplicated which also 
resulted in one number going missing. Find both these numbers.

Example 1:
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Example 2:
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
'''
def solution(array):

	i = 0

	while i < len(array):
		j = array[i] - 1

		if array[i]!=array[j]:
			array[i], array[j] = array[j], array[i]
		else:
			i+=1

	result = []

	for i in range(len(array)):
		if array[i] != (i+1):			
			result.append(array[i])
			result.append(i+1)

	return result

print('Result: ', solution([3, 1, 2, 5, 2]))
print('Result: ', solution([3, 1, 2, 3, 6, 4]))