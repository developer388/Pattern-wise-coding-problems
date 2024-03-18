'''
Given an unsorted array containing numbers, find the smallest missing 
positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'.

Example 2:
Input: [3, -2, 0, 1, 2]
Output: 4

Example 3:
Input: [3, 2, 5, 1]
Output: 4
'''
def solution(array):
	i = 0

	while i<len(array):
		j = array[i]-1
		if array[i]>0 and array[i]<=len(array) and  array[i] != array[j]:
			array[i], array[j] = array[j], array[i]
		else:
			i+=1

		print(array)

	for i in range(len(array)):
		if array[i] != (i+1):
			return i+1


print('Result: ', solution([-3, 1, 5, 4, 2]))

print('Result: ', solution([3, -2, 0, 1, 2]))

print('Result: ', solution([3, 2, 5, 1]))

