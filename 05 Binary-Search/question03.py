'''
Given an array of lowercase letters sorted in ascending order, 
find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter 
is assumed to be connected with the first letter. This also means that the smallest
letter in the given array is greater than the last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given ‘key’.

Example 1:

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
Example 4:

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.


Observation:
	when array[mid] == key is set to 
			start = mid+1

	at the end of loop, mid will point to 
	value greater than search value

'''




def solution(array, key):

	if key < array[0] or key > array[-1]:
		return array[0]

	start = 0
	end = len(array) - 1

	while start <= end:

		mid = (start +  end) // 2
		
		if key < array[mid]:
			end = mid - 1
		elif key > array[mid]:
			start = mid + 1
		else:
			start = mid + 1

	return array[start % len(array)]


print('Result: ', solution(['a', 'c', 'f', 'h'], 'm' ))