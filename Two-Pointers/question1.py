'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target. 
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

	Input: [1, 2, 3, 4, 6], target=6

	Output: [1, 3]

	Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:

	Input: [2, 5, 9, 11], target=11
	
	Output: [0, 2]
	
	Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

Leetcode URL: https://leetcode.com/problems/two-sum/

'''


'''
Solution 1: Optimized Approach 1
	
	As array is sorted, we can start pointer from start and end.

	start first_pointer from beginning
	start second_pointer from end

	compare sum of both the pointers with target

	if sum_of_pointer is greater than target
	    decrement the second_pointer

	if sum_of_pointer is less than target
	    increment the first_pointer

'''



def mainSolution(array, target):

	first_pointer = 0
	second_pointer = len(array) - 1

	while first_pointer != second_pointer:
		sum_of_pointers = array[first_pointer] + array[second_pointer]
		if sum_of_pointers > target:
			second_pointer -= 1
		elif sum_of_pointers < target:
			first_pointer +=1
		else:
			return [first_pointer, second_pointer]

	return []



print("Result using mainSolution: ", mainSolution([1, 2, 3, 4, 6], 6))

print("Result using mainSolution: ", mainSolution([2, 5, 9, 11], 1))

