'''

Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].


approach:
	
	if value of second_pointer != value of first_pointer
		increment the first_pointer and sets its value to second_pointer


'''


def solution(array):
	first_pointer = 0
	
	for second_pointer in range(1, len(array)):

		if array[second_pointer] != array[first_pointer]:
			first_pointer += 1
			array[first_pointer] = array[second_pointer]


	print(array)
	print(first_pointer, second_pointer)
	return first_pointer + 1

print('Result:', solution([2, 2, 2, 11]))
