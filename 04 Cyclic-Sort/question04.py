'''
We are given an unsorted array containing ‘n+1’ numbers 
taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. You are, however,
 allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
'''

def solution(array):
	i = 0
	while i<len(array):
		
		if array[i] != (i+1):				
			j = array[i]-1

			if array[i]!=array[j]:
				array[i], array[j] = array[j], array[i]
			else:
				return array[i]

		else:
			i+=1




print('Solution: ', solution([1, 4, 4, 3, 2]))
print('Solution: ', solution([2, 1, 3, 3, 5, 4]))
print('Solution: ', solution([2, 4, 1, 4, 4]))