'''
Given an array arr of unsorted numbers and a target sum, count all triplets in it 
such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
Write a function to return the count of such triplets.

Example 1:

	Input: [-1, 0, 2, 3], target=3 

	Output: 2

	Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]


Example 2:

	Input: [-1, 4, 2, 1, 3], target=5 

	Output: 4

	Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

#important
'''

'''
Solution 1: Brute Force Approach

	In this approach we are using three nested loops, and if sum of a triplet indicated by i, j, k is less than target
		we increment the result count variable


Time Complexity: O(n^3)
'''


def bruteForceSolution(array, target):

    result = 0
    
    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                
                if array[i]+array[j]+array[k] < target:
                    result+=1
    return result

print("Result using BruteForceSolution: ", bruteForceSolution([-1, 0, 2, 3], 3))
print("Result using BruteForceSolution: ", bruteForceSolution([-1, 4, 2, 1, 3], 5))



'''
Solution 2: Optimized Approach

	If we sort the given array, we can take advantage of the two pointer approach to efficiently find a triplet

	we have first_pointer starting from 0 to array.length - 2 and

	a second_pointer and third_pointer starting from first_pointer + 1 and end of the array respectively.

	
	if first_pointer + sum_two_pointers equals is less than target
		
		Because we need the count of triplets here and because we have sorted the array
		if sum_of_three pointer is less than target, moving the third_pointer from right to left we always shorten our sum
		and therefore we can consider window_sum of second_pointer and third_pointer to consider all of the triplets
		ideally window length is calculated as (second_pointer-first_pointer)+1, because in this case window_length is inclusive
		of second and third pointer and it cannot be less than two we can consider second_pointer - first_pointer as the window sum

		once we have stored window_length in our result variable, we want to increase the three_pointer_sum
		so we do second_pointer += 1

	if sum of first_pointer + sum_two_pointers is greater than or equal to target
	    we want to decrease the window_sum by decreasing third_pointer
	    third_pointer -= 1

Time Complexity: O(n^2)

The outer loop iterates over each element of the array once, resulting in O(n) iterations.
Inside the outer loop, there's a two-pointer approach that iterates through the remaining elements of the array. 
This also results in O(n) iterations in the worst case.

'''

def mainSolution(array, target):

	array.sort()

	result = 0

	for first_pointer in range(len(array)-2):

		second_pointer = first_pointer + 1
		third_pointer = len(array) - 1

		while second_pointer < third_pointer:

			if array[first_pointer] + array[second_pointer] + array[third_pointer] < target:
				result += (third_pointer - second_pointer)
				second_pointer += 1
			else:
				third_pointer -= 1
	
	return result
			

print("Result using mainSolution: ", mainSolution([-1, 0, 2, 3], 3))
print("Result using mainSolution: ", mainSolution([-1, 4, 2, 1, 3], 5))