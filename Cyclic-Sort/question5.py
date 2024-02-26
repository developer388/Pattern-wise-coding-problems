'''
We are given an unsorted array containing ‘n’ numbers taken from the 
range 1 to ‘n’. The array has some duplicates, find all the duplicate 
numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]

'''

def solution(array):

	i = 0

	while i < len(array):
		j = array[i]-1

		if array[i]!=array[j]:
			array[i], array[j] = array[j], array[i]
		else:
			i+=1

	print(array)

	result = []

	for i in range(len(array)):
		if array[i]!= (i+1):
			result.append(array[i])


	return result
print('Result: ', solution([3, 4, 4, 5, 5]))
print('Result: ', solution([5, 4, 7, 2, 3, 5, 3]))