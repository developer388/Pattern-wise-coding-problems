'''
Given an array of positive numbers and a positive number ‘k’.
Find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

	Input: [2, 1, 5, 1, 3, 2], k=3 
	
	Output: 9

	Explanation: Subarray with maximum sum is [5, 1, 3].

'''


'''
Solution 1: Brute Force Approach
	
	outer loop from i=0 to i=end of string
	   inner loop from j=i to j=end of string
	      if window_size === k
	      	 result = max(result, window_sum)
'''

def bruteForceSolution(array, k):
    result = 0
    for i in range(len(array)):
        window_sum = 0
        for j in range(i, len(array)):
            window_sum += array[j]
            
            if ((j-i)+1  == k):
                result = max(result, window_sum)
    return result


print("Result using BruteForceSolution: ", bruteForceSolution([2, 1, 5, 1, 3, 2], 3))

"""
Solution 2: Optimized Approach 1
	
	second_pointer will increase the window_sum

	if window_size > k:
		subtract array[first_pointer] from the window sum
		
		increase the first_pointer
	
	result = max(result, window_sum)
"""

def mainSolution(array, k):

	first_pointer = 0
	second_pointer = 0

	window_sum = 0

	result = 0

	for second_pointer in range(len(array)):

		window_sum += array[second_pointer]

		if (second_pointer-first_pointer)+1 > k:
			window_sum -= array[first_pointer]
			first_pointer +=1

		
		result = max(result, window_sum)

	return result


print("Result using mainSolution: ", mainSolution([2, 1, 5, 1, 3, 2], 3))


'''
Solution 3: Optimized Approach 2
	
	we can also increase first_pointer if second_pointer > k -1

'''
def solution2(array, k):

	first_pointer = 0
	second_pointer = 0

	window_sum = 0

	result = 0

	for second_pointer in range(len(array)):

		window_sum += array[second_pointer]		
	
		if second_pointer > k-1:
			window_sum -= array[first_pointer]
			first_pointer +=1

		
		result = max(result, window_sum)

	return result

print("Result using Solution2: ", solution2([2, 1, 5, 1, 3, 2], 3))
