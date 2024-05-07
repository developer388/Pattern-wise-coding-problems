'''

Given a collection of numbers, that might contain duplicates, return all possible unique permutations in any order.
Example:

Input: [1,1,2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]


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


print('Result: ', solution([1,1,2], [], 0))