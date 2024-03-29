'''
We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
 The array can have duplicates, which means some numbers will be missing. 
 Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4
'''


def solution(array):

	i = 0

	while i<len(array):

		j = array[i]-1

		if  array[i]!=array[j]:
			array[i], array[j] = array[j], array[i]
		else:
			i += 1

	print(array,i)

	result = []

	for i in range(len(array)):
		if array[i] != (i+1):
			result.append(i+1)

	return result



print('Result: ', solution([2, 3, 1, 8, 2, 3, 5, 1]))
print('Result: ', solution([2, 3, 2, 1]))
print('Result: ', solution([2, 4, 1, 2]))