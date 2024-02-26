'''
Given an array of numbers which is sorted in ascending order 
and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array.
If the ‘key’ is not present, return -1. You can assume that the given array does 
not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
'''

def solution(array, key):
	start = 0
	end = len(array)-1

	while start<=end:

		mid = (start + end) // 2

		if key == array[mid]:
			return mid

		if array[start] <= array[mid]:

			if key >= array[start] and key < array[mid]:
				end = mid - 1
			else:
				start = mid + 1

		else:
		 	if key > array[mid] and key <= array[end]:
		 		start = mid + 1
		 	else:
		 		end = mid - 1
	return -1



print('Result: ', solution([10, 15, 1, 3, 8], 15))
print('Result: ', solution([4, 5, 7, 9, 10, -1, 2], 2))