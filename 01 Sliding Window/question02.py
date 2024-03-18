'''
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0, if no such subarray exists.

Example 1:

	Input: [2, 1, 5, 2, 3, 2], S=7 

	Output: 2

	Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Leetcode URL: https://leetcode.com/problems/minimum-size-subarray-sum/
'''


'''
Solution 1: Brute Force Approach
	
	outer loop from i=0 to i=end of string
	   inner loop from j=i to j=end of string
	      if window_sum >= k
	      	 result = max(result, window_size)

'''
def bruteForceSolution(arr, s):
    
    window_size = len(arr)
    
    for i in range(len(arr)):
        
        window_sum = 0
        
        for j in range(i, len(arr)):
            
            window_sum += arr[j]
            
            if window_sum >= s:
                window_size = min(window_size, (j-i)+1)
        
        
    return window_size

    
print("Result using BruteForceSolution: ", bruteForceSolution([2, 1, 5, 2, 3, 2], 7 ))  


'''
Solution 2: Optimized Approach 1
    
    Approach Info:

	observation:
		window size is not fixed

		sliding window will shrink, if window_sum >= target

		for second pointer at ith position, if window size needs to be shrink
		we require a while loop to increment first_pointer, second_pointer will remain fixed

'''

def mainSolution(nums, target):

	first_pointer = 0
	second_pointer = 0

	result = len(nums)

	window_sum = 0

	for second_pointer in range(len(nums)):
		window_sum += nums[second_pointer]

		while window_sum>=target:
			result = min(result, (second_pointer-first_pointer)+1)
			window_sum -= nums[first_pointer]
			first_pointer += 1

	return result


print("Result using mainSolution: ", , mainSolution([2, 1, 5, 2, 3, 2], 7))
print("Result using mainSolution: ", , mainSolution([1,4,4], 4))
print("Result using mainSolution: ", , mainSolution([2,3,1,2,4,3], 7))
print("Result using mainSolution: ", , mainSolution([1,2,3,4,5], 11))


 





