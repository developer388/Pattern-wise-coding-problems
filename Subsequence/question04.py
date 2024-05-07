'''
Generate one subsequences of the given array whose sum equals to K

Input: arr[] = {1, 2, 3}, K = 3 
Output: 
1 2 

'''


def solution(input_array, sub_array, subarray_sum, result, i, k):

	if (subarray_sum == k):
		result.append(list(sub_array))
		return True

	if i==len(input_array):
		return result

	sub_array.append(input_array[i])
	subarray_sum += input_array[i]
	
	if solution(input_array, sub_array, subarray_sum, result, i+1, k):
		return result

	sub_array.pop()
	subarray_sum -= input_array[i]
	
	if solution(input_array, sub_array, subarray_sum, result, i+1, k):
		return result

	return False




print('Result: ', solution([1,2,3], [], 0, [], 0, 3))