'''
Given a Bitonic array, find if a given ‘key’ is present in it. 
An array is considered bitonic if it is monotonically increasing and then 
monotonically decreasing. Monotonically increasing or decreasing means that for
 any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3
Example 2:

Input: [3, 8, 3, 1], key=8
Output: 1
Example 3:

Input: [1, 3, 8, 12], key=12
Output: 3
Example 4:

Input: [10, 9, 8], key=10
Output: 0

'''
def find_max(array):

	start = 0
	end = len(array) - 1

	while start <= end:

		mid = (start + end) // 2

		if mid+1 > len(array)-1:
			return start
			
		if array[mid] <= array[mid+1]:
			start = mid + 1
		else:
			end = mid - 1
		
	return start

def search(start, end, array, key):

	while start<=end:
		mid = (start+end)//2

		if key == array[mid]:
			return mid

		if array[start]<array[end]:				
			if key < array[mid]:
				end = mid - 1
			elif key > array[mid]:
				start = mid + 1
		else:
			if key < array[mid]:
				start = mid + 1
			elif key > array[mid]:
				end = mid - 1

	return -1


def solution(array, key):
	
	max_index = find_max(array)
	result = search(0, max_index, array, key)
	if result == -1:
		result = search(max_index, len(array)-1, array, key)

	return result

	
print('\nResult: ', solution([1, 3, 8, 4, 3], 4))
print('\nResult: ', solution([3, 8, 3, 1], 8))
print('\nResult: ', solution([1, 3, 8, 12], 12))
print('\nResult: ', solution([10, 9, 8, 5], 8))