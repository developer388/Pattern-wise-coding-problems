'''
Given an array of numbers sorted in ascending order, 
find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
'''

def solution(array, key):

	print('input: ', array, 'target: ', key)


	if key < array[0]:
		return array[0]
	elif key > array[-1]:
		return array[-1]

	start = 0
	end = len(array) - 1

	while start<=end:

		mid = (start+end)//2
		if key < array[mid]:
			end = mid - 1
		elif key > array[mid]:
			start = mid + 1
		else:
			return array[mid]


	if (key - array[start]) > (key - array[end]):
		return array[start]
	else:
		return array[end]


	return start, mid, end
	

print('Result: ', solution([4, 6, 10], 7))

print('Result: ', solution([4, 6, 10], 11))
print('Result: ', solution([4, 6, 10], 4))


print('Result: ', solution([1, 3, 8, 10, 15], 12))


print('Result: ', solution([4, 6, 10], 3))
print('Result: ', solution([4, 6, 10], 17))