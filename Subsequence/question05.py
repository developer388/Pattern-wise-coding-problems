'''
Find number of subsequences of the given array

Input: arr[] = {1, 2, 3}, K = 3 
Output: 
1 2 

'''


def solution(input_array, i):

	if i == len(input_array):
		return 1

	
	take = solution(input_array, i+1)

	not_take = solution(input_array, i+1)
	
	return take + not_take




print('Result: ', solution([1,2,3], 0))