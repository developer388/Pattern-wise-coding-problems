'''
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.

Example 2:

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.

Example 3:

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.

'''
def solution(array):
	start = 0
	end = len(array) - 1

	while start <= end:

		mid = (start + end) // 2

		print(f'start:{start}, mid:{mid}, end: {end}')

		if array[start] < array[mid]:
			#asc
			start = mid + 1
		else:
			end = mid - 1

		if end+1 < len(array) and array[end]>array[end+1]:
			print('rotated by: ')
			return ( (len(array)-1) - (end + 1))+1

		
	return 0

#print('Result: ', solution([10, 15, 1, 3, 8]))

#print('Result: ', solution([4, 5, 7, 9, 10, -1, 2]))
print('Result: ', solution([11,12,1, 3, 8, 10]))