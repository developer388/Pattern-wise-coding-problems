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

Leetcode URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''


'''
Solution 1: Optimized Approach 1
		
	start both the pointers from the start of the array

	if value of second_pointer != value of first_pointer
		increment the first_pointer and sets its value to second_pointer

	return window sum


Time Complexity: O(n)

The for loop iterates over each element of the array once, resulting in O(n) iterations.
'''


def mainSolution(array):
	first_pointer = 0
	
	for second_pointer in range(1, len(array)):

		if array[second_pointer] != array[first_pointer]:
			first_pointer += 1
			array[first_pointer] = array[second_pointer]

	return (first_pointer - 0) + 1

print("Result using mainSolution: ", mainSolution([2, 2, 2, 11]))
