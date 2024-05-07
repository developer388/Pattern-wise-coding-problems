'''
Find number of  subsequences of the given array with sum equals to K

Input: arr[] = {1, 2, 3}, K = 3 
Output: 
1 2 
3

'''


def solution(input_array, subarray_sum, i, k):
	

	if i == len(input_array):
		if (subarray_sum == k):
			return 1
		return 0

	subarray_sum += input_array[i]
	take = solution(input_array, subarray_sum,  i+1, k)

	subarray_sum -= input_array[i]
	not_take = solution(input_array, subarray_sum,  i+1, k)

	return take + not_take




print('Result: ', solution([1,2,3], 0, 0, 3))