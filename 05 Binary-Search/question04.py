'''
Given an array of numbers sorted in ascending order, 
find the range of a given number ‘key’. The range of the ‘key’ 
will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]

Observation:

	if there are duplicate values in a sorted array
	
	if number == array[mid]:
		start = mid + 1

	    when loop ends start will point to last occurrence of number

	if number == array[mid]:
		end = mid - 1

		when loop ends start will point to first occurrence of number


'''


def search(array, key, find_min_index):

	start = 0
	end = len(array) - 1
	key_index = -1

	while start<=end:

		mid = (start+end) // 2

		if key < array[mid]:
			end = mid - 1
		elif key > array[mid]:
			start = mid + 1
		else:
			key_index = mid
			if find_min_index:
				end = mid - 1
			else:
				start = mid + 1

	return key_index

def solution(array, key):
	min_index = search(array, key, True)
	max_index = search(array, key, False)
	return [min_index, max_index]


print('Result: ', solution([4, 6, 6, 6, 9], 6))
print('Result: ', solution([1, 3, 8, 10, 15], 11))