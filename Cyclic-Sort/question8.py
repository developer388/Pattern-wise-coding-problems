'''

Given an unsorted array containing numbers and a number ‘k’, 
find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
'''

def solution(array, k):
	i = 0
	while i<len(array):
		j = array[i] - 1
		if array[i]>0 and array[i]<=len(array) and array[i]!=array[j]:
			array[i], array[j] = array[j], array[i]
		else:
			i+=1
		print(array)


print('Result: ', solution([3, -1, 4, 5, 5], 3))

# print('Result: ', solution([2, 3, 4], 3))

# print('Result: ', solution([-2, -3, 4],2))

