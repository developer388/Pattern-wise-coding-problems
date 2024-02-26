'''

Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

https://leetcode.com/problems/minimum-size-subarray-sum/
'''

'''
	observation:
		window size is not fixed

		sliding window will shrink, if window_sum >= target

		for second pointer at ith position, if window size needs to be shrink
		we require a while loop to increment first_pointer, second_pointer will remain fixed

'''

def solution(nums, target):

	first_pointer = 0
	second_pointer = 0

	minimum_window_size = len(nums)

	window_sum = 0

	for second_pointer in range(len(nums)):
		window_sum += nums[second_pointer]

		while window_sum>=target:
			minimum_window_size = min(minimum_window_size, (second_pointer-first_pointer)+1)
			window_sum -= nums[first_pointer]
			first_pointer += 1

		
			

	return minimum_window_size


print('Solution: ', solution([2, 1, 5, 2, 3, 2], 7 ))

print('Solution: ', solution([1,4,4], 4 ))

print('Solution: ', solution([2,3,1,2,4,3], 7 ))


print('Solution: ', solution([1,2,3,4,5], 11 ))







