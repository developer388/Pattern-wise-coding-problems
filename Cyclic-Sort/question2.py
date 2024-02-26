'''
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, 
find the missing number.

Example 1:

Input: [4, 0, 3, 1]
	   [1, 0, 3, 4]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

'''


def solution(array):

	i = 0
	
	while i < len(array):
		j = array[i]

		if array[i] < len(array) and array[i]!=array[j]:
			array[i], array[j] = array[j], array[i]			
		else:
			i+=1
		print(array, i)

	for i in range(len(array)):
		if array[i] != i:
			return i






print('Result: ', solution( [8, 3, 5, 2, 4, 6, 0, 1]))
