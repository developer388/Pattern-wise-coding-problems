'''
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation:
	2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
	7 is a candidate, and 7 = 7.
	
	These are the only two combinations.
'''

def solution(input_array, target, i, sub_array, result):

	if i == len(input_array):
		if target == 0:
			result.append(list(sub_array))

		return result

	if input_array[i] <= target:
		
		sub_array.append(input_array[i])
		target -= input_array[i]
		
		solution(input_array, target, i, sub_array, result)
		
		sub_array.pop()
		target += input_array[i]
	
	solution(input_array, target, i+1, sub_array, result)

	return result


print('Result: ', solution([2,3,6,7],7, 0, [], []))