'''
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example:
Input: [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''

def solution(input_array, result, index):

	if index == len(input_array):
		result.append(list(input_array))
		return result


	for i in range(index, len(input_array)):
		input_array[index], input_array[i] = input_array[i], input_array[index]
		solution(input_array, result, index+1)

		input_array[index], input_array[i] = input_array[i], input_array[index]
	
	return result


print('Result: ', solution([1,2,3], [], 0))