'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’. Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9

Explanation: Subarray with maximum sum is [5, 1, 3].

'''

''' 
	observation
		window size is fixed

	we are checking if second_pointer exceeds window size
	window_size = (second_pointer-first_pointer)+1
'''
def solution(nums, k):

	first_pointer = 0
	second_pointer = 0

	window_sum = 0

	result = 0

	for second_pointer in range(len(nums)):

		window_sum += nums[second_pointer]		

		window_size = (second_pointer-first_pointer)+1

		if window_size > k:
			window_sum -= nums[first_pointer]
			first_pointer +=1

		
		result = max(result, window_sum)

	return result



# we are checking if second_pointer exceeds index
def solution2(nums, k):

	first_pointer = 0
	second_pointer = 0

	window_sum = 0

	result = 0

	for second_pointer in range(len(nums)):

		window_sum += nums[second_pointer]		
	
		if second_pointer > k-1:
			window_sum -= nums[first_pointer]
			first_pointer +=1

		
		result = max(result, window_sum)

	return result


print('Result1: ', solution([2, 1, 5, 1, 3, 2], 3))
print('Result2: ', solution2([2, 1, 5, 1, 3, 2], 3))
