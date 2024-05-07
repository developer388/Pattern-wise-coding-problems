'''
Generate all subsequences of an array with sum equals to K

Input: arr[] = {1, 2, 3}, K = 3 
Output: 
1 2 
3

'''


def solution(input_array, sub_array, subarray_sum, result, i, k):
	
	if (subarray_sum == k):
		result.append(list(sub_array))
		return result

	if i==len(input_array):
		return result

	sub_array.append(input_array[i])
	subarray_sum += input_array[i]
	result = solution(input_array, sub_array, subarray_sum, result, i+1, k)

	sub_array.pop()
	subarray_sum -= input_array[i]
	result = solution(input_array, sub_array, subarray_sum, result, i+1, k)

	return result




# print('Result: ', solution([1,2,3], [], 0, [], 0, 3))



print('Result: ', solution([10,1,2,7,6,1,5], [], 0, [], 0, 8))