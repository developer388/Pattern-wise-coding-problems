'''
Problem 1: Given an unsorted array of numbers and a target ‘key’, 
remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
	   [2,6,3]
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].


approach:
	
	if value of second_pointer != key
		increment the first_pointer and sets its value to second_pointer


'''

def solution(array, key):

	first_pointer = - 1

	for second_pointer in range(len(array)):

		if (array[second_pointer] != key):
			first_pointer += 1
			array[first_pointer] = array[second_pointer]
	
	print(array, first_pointer)


	return first_pointer+1


print('Result: ', solution([3, 2, 3, 6, 3, 10, 9, 3], 3))
print('Result: ', solution([2, 11, 2, 2, 1], 2))