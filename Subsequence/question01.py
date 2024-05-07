'''

Question: Generate all subsequences of an array

Approach: For every element in the array, there are two choices, either to include it in the subsequence or not include it. 
Apply this for every element in the array starting from index 0 until we reach the last index. Print the subsequence once the last index is reached. 

'''
def solution(input_array, sub_array, result, i):

	if i == len(input_array):
		result.append(list(sub_array))
		return result

	sub_array.append(input_array[i])
	result = solution(input_array, sub_array,result, i+1)
	
	sub_array.pop()
	result = solution(input_array, sub_array,result, i+1)

	return result



print('Result: ', solution([1,2,3], [], [], 0))

