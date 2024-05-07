'''
Generate one subsequence of the given array whose sum equals to K.


Example :

Input: [1, 2, 3], K = 3 
Output: [[1,2]]

Explanation: Sum of both [1,2] and [3] is equivalent to K, but as mentioned in question 
we need to consider only one subsequence.
'''

def solution(input_array, k, sub_array, sum_of_subsequence, result, index):

	if index == len(input_array):
		if sum_of_subsequence == k:
			result.append(sub_array)
			return True

		return False


	sub_array.append(input_array[index])
	sum_of_subsequence += input_array[index]

	if (solution(input_array, k, sub_array, sum_of_subsequence, result, index+1)):
		return result


	sub_array.pop()
	sum_of_subsequence -= input_array[index]

	if (solution(input_array, k, sub_array, sum_of_subsequence, result, index+1)):
		return result

	return False

print('Result: ', solution([1, 2, 3], 3, [], 0, [], 0))