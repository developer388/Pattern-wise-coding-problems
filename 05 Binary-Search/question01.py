'''
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted,
we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
Example 2:

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Example 3:

Input: [10, 6, 4], key = 10
Output: 0
Example 4:

Input: [10, 6, 4], key = 4
Output: 2

'''

def solution(array, target):


	sorted_by_asc_order = array[0] < array[-1]

	start = 0
	end = len(array) - 1
	
	while start<=end:

		mid = (end + start) // 2
		
		if array[mid] < target:
			
			if sorted_by_asc_order:
				start = mid+1
			else:
				end = mid - 1
		
		elif array[mid] > target:
			if sorted_by_asc_order:
				end = mid - 1
			else:
				start = mid + 1
		else:
			return mid 

		print('start:', start, 'end:', end)


	return -1



#print('Result: ', solution([1, 2, 3, 4, 5, 6, 7], 5))

#print('Result: ', solution([10, 6, 4], 4))



def binary_search(array, number):

	start = 0
	end = len(array) - 1


	while start <= end:

		mid = (start+end) // 2

		print('mid: ', mid)

		if number < array[mid]:
			end = mid - 1
		elif number > array[mid]:
			start = mid + 1
		else:
			print(f'Loop Completed: True Start: {start}, Mid: {mid}, End: {end}')
			return True
	
	print(f'Loop Completed: False Start: {start}, Mid: {mid}, End: {end}')

	return False


print('BinarySearch: ', binary_search([11,12,14,19,21], 20))