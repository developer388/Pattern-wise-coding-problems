'''
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, 
whose sum is equal to the target number.


Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.


https://leetcode.com/problems/4sum/
'''


def solution(array, target):

	array.sort()

	result = []

	print('array: ', array)

	for first_pointer in range(len(array)):

		if first_pointer > 0 and array[first_pointer] == array[first_pointer -1]:
			continue

		for second_pointer in range(first_pointer+1,  len(array)):

			if second_pointer != first_pointer+1 and array[second_pointer] == array[second_pointer -1]:
				continue

			third_pointer = second_pointer + 1
			fourth_pointer = len(array) - 1

			while third_pointer < fourth_pointer:

				four_pointer_sum = array[first_pointer] + array[second_pointer] + array[third_pointer] + array[fourth_pointer]

				if four_pointer_sum > target:
					fourth_pointer -= 1
				elif four_pointer_sum < target:
					third_pointer += 1
				else:
					result.append([array[first_pointer], array[second_pointer], array[third_pointer], array[fourth_pointer]])
					third_pointer += 1
					fourth_pointer -= 1

					while third_pointer<fourth_pointer and  array[third_pointer] == array[third_pointer-1]:
						third_pointer += 1

					while fourth_pointer < len(array)-2 and array[fourth_pointer] == array[fourth_pointer+1]:
						fourth_pointer -= 1

	return result


print('Result: ', solution([4, 1, 2, -1, 1, -3], 1))
print('Result: ', solution([2, 0, -1, 1, -2, 2], 2))
print('Result: ', solution([2, 2, 2, 2, 2], 8))



# https://www.youtube.com/watch?v=eD95WRfh81c