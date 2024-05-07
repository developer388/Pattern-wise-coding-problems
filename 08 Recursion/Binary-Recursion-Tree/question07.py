'''
Find number of subsequences of a given array with sum equals to K.

Example :
Input: [1, 2, 3], K = 3 
Output: 2

'''

def solution(input_array, k, sum_of_subsequence, index):

	if index == len(input_array):

		if sum_of_subsequence == k:
			return 1

		return 0


	sum_of_subsequence += input_array[index]	
	result1 = solution(input_array, k, sum_of_subsequence, index+1)

	sum_of_subsequence -= input_array[index]
	result2 = solution(input_array, k, sum_of_subsequence, index+1)

	return result1 + result2



print('Result: ', solution([1,2,3], 3, 0, 0))