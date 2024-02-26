'''
Given an array arr of unsorted numbers and a target sum, Write a function to return the list of all triplets
such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: [[-1, 0, 3], [-1, 0, 2]]
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Input: [-1, 4, 2, 1, 3], target=5 
Output: [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]
Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
'''
'''
Approach:
	Use three pointers	
'''


def solution(array, target):


	array.sort()

	print('array: ', array, 'target: ', target)

	result = []

	for first_pointer in range(len(array)-2):

		second_pointer = first_pointer + 1
		third_pointer = len(array) - 1

		while second_pointer < third_pointer:

			three_pointer_sum = array[first_pointer] + array[second_pointer] + array[third_pointer]

			if three_pointer_sum < target:
				
				for i in range(third_pointer, second_pointer, -1):
					result.append([array[first_pointer], array[second_pointer], array[i]])

				second_pointer += 1
			else:
				third_pointer -= 1
	
	return result
			

print('Result: ', solution([-1, 0, 2, 3], 3))
print('Result: ', solution([-1, 4, 2, 1, 3], 5))