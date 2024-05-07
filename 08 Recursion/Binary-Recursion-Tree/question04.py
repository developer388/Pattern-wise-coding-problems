'''
Generate all subsequences of a given array with sum equals to K.

Example :
Input: [1, 2, 3], K = 3 
Output: [[1,2], [3]]

'''

def solution(input_array, k, sub_array, sum_of_subsequence, result, index):

	if index == len(input_array):
		
		if sum_of_subsequence == k:
			result.append(list(sub_array))
		
		return result

	sub_array.append(input_array[index])
	sum_of_subsequence += input_array[index]
	solution(input_array, k, sub_array, sum_of_subsequence, result, index+1)

	
	sub_array.pop()
	sum_of_subsequence -= input_array[index]
	solution(input_array, k, sub_array, sum_of_subsequence, result, index+1)

	return result




print('Result: ', solution([1,2,3], 3, [], 0, [], 0))