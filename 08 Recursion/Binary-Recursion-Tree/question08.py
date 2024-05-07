'''
Given an array of distinct integers candidates and a target integer, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example :
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. 

Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7. 
These are the only two combinations.
'''

def solution(input_array, target, subsequence, result, index):

	if index == len(input_array):

		if target == 0:
			result.append(list(subsequence))

		return result

	if input_array[index] <= target:
		subsequence.append(input_array[index])
		target -= input_array[index]
		solution(input_array, target, subsequence, result, index)

		subsequence.pop()
		target += input_array[index]


	solution(input_array, target, subsequence, result, index+1)

	return result


print('Result: ', solution([2,3,6,7], 7, [], [], 0))