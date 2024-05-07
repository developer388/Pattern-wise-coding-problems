'''
Generate sum of all subsequences of a given array.

Example :
 Input: [1, 2, 3]
 Output: [0, 3, 2, 5, 1, 4, 3, 6]

'''

def solution(input_array, sum_of_subsequence, result, index):

	if index == len(input_array):
		result.append(sum_of_subsequence)
		return

	sum_of_subsequence += input_array[index]
	solution(input_array, sum_of_subsequence, result, index+1)


	sum_of_subsequence -= input_array[index]
	solution(input_array, sum_of_subsequence, result, index+1)

	return result


print('Result: ', solution([1, 2, 3], 0, [], 0))