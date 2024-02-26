'''
Given an array of unsorted numbers and a target number, find a triplet in the array whose
sum is as close to the target number as possible, return the sum of the triplet. If there
are more than one such triplet, return the sum of the triplet with the smallest sum.


Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

'''

'''

Approach:
	Use three pointers	

'''


def solution(array, target):


	array.sort()

	result = float('-inf')

	for first_pointer in range(len(array)-2):

		second_pointer = first_pointer + 1
		third_pointer = len(array) - 1


		required_two_pointer_sum = target - array[first_pointer]

		while second_pointer < third_pointer:

			two_pointer_sum = array[second_pointer] + array[third_pointer]

			if two_pointer_sum > required_two_pointer_sum:
				third_pointer -= 1
			elif two_pointer_sum <= required_two_pointer_sum:
				result = max(result, array[first_pointer] + array[second_pointer] + array[third_pointer])				
				second_pointer += 1
	
	return result
			

print('Result: ', solution([-2, 0, 1, 2], 2))
print('Result: ', solution([-3, -1, 1, 2], 1))
print('Result: ', solution([1, 0, 1, 1], 100))


















