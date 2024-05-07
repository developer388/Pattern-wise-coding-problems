'''
Generate all subsequences of a given array.

Example :
 Input: [1, 2, 3]
 Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

'''

def solution(input_array, sub_array, result, index):

	if index == len(input_array):
		result.append(list(sub_array))
		return result

	sub_array.append(input_array[index])
	solution(input_array, sub_array, result, index+1)

	sub_array.pop()
	solution(input_array, sub_array, result, index+1)

	return result

print('Result: ', solution([1, 2, 2], [], [], 0))