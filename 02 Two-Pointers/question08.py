'''
Given an array arr of unsorted numbers and a target sum, Write a function to return the list of all triplets
such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 

Example 1:

	Input: [-1, 0, 2, 3], target=3 

	Output: [[-1, 0, 3], [-1, 0, 2]]

	Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]


Example 2:
	
	Input: [-1, 4, 2, 1, 3], target=5 
	
	Output: [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]
	
	Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
'''


'''
Solution 1: Brute Force Approach

	In this approach we are using three nested loops, and if sum of a triplet indicated by i, j, k is less than target
		we add the triplet to our result variable


Time Complexity: O(n^3)	
'''

def bruteForceSolution(array, target):
    
    result = []
    
    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                
                if array[i] + array[j] + array[k] < target:
                    result.append([array[i] , array[j] , array[k]])      
        
    
    return result
	
print("Result using BruteForceSolution: ", bruteForceSolution([-1, 0, 2, 3], 3))
print("Result using BruteForceSolution: ", bruteForceSolution([-1, 4, 2, 1, 3], 5))


'''
Solution 2: Optimized Approach

	If we sort the given array, we can take advantage of the two pointer approach to efficiently find a triplet

	we have first_pointer starting from 0 to array.length - 2 and

	a second_pointer and third_pointer starting from first_pointer + 1 and end of the array respectively.

	
	if first_pointer + sum_two_pointers equals is less than target
		
		we add the triplet to our result

	    we want to increase the three_pointer_sum so
		we do second_pointer += 1

	if sum of first_pointer + sum_two_pointers is greater than or equal to target
	    we want to decrease the window_sum by decreasing third_pointer so
	    we do third_pointer -= 1

Time Complexity: O(n^2)

The outer loop iterates over each element of the array once, resulting in O(n) iterations.
Inside the outer loop, there's a two-pointer approach that iterates through the remaining elements of the array. 
This also results in O(n) iterations in the worst case.

'''
def mainSolution(array, target):


	array.sort()

	print('array: ', array, 'target: ', target)

	result = []

	for first_pointer in range(len(array)-2):

		second_pointer = first_pointer + 1
		third_pointer = len(array) - 1

		while second_pointer < third_pointer:

			three_pointer_sum = array[first_pointer] + array[second_pointer] + array[third_pointer]

			if three_pointer_sum < target:
				
				for i in range(third_pointer, second_pointer, -1):
					result.append([array[first_pointer], array[second_pointer], array[i]])

				second_pointer += 1
			else:
				third_pointer -= 1
	
	return result
			

print('Result: ', mainSolution([-1, 0, 2, 3], 3))
print('Result: ', mainSolution([-1, 4, 2, 1, 3], 5))