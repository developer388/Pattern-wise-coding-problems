'''
Find number of subsequences of a given array

Example :
Input: [1, 2, 3]
Output: 8

'''

def solution(input_array, index):

	if index == len(input_array):
		return 1

	result1 = solution(input_array, index+1)

	result2 = solution(input_array, index+1)

	return result1 + result2


print('Result: ', solution([1,2,3], 0))