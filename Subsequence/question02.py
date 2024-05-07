'''
Generate sum of all subsequences of the given array

'''

def solution(input_array, subarray_sum, result, i):

	if i == len(input_array):
		result.append(subarray_sum)
		return

	subarray_sum += input_array[i]
	solution(input_array, subarray_sum, result, i+1)

	subarray_sum -= input_array[i]
	solution(input_array, subarray_sum, result, i+1)

	return result





print('Result: ', solution([1,2,3], 0, [], 0))