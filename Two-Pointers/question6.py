'''
Given an array of unsorted numbers and a target number, find a triplet in the array whose
sum is as close to the target number as possible, return the sum of the triplet. If there
are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

	Input: [-2, 0, 1, 2], target=2
	
	Output: 1

	Explanation: The triplet [-2, 1, 2] has the closest sum to the target.


Example 2:

	Input: [-3, -1, 1, 2], target=1

	Output: 0

	Explanation: The triplet [-3, 1, 2] has the closest sum to the target.


Example 3:

	Input: [1, 0, 1, 1], target=100
	
	Output: 3
	
	Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''

'''
Solution 1: Brute Force Approach

	In this approach we are using three nested loops, and if sum of a triplet indicated by i, j, k <= 0
		we store it in result variable

	We need nearest value to target, which means it can less than or equal to target.
		we are considering a triplet if it is less than or equal to target
		we have used max() function to store the nearest value in result variable

Time Complexity: O(n^3)
'''


def bruteForceSolution(array, target):

    result = float('-inf')

    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                
                if array[i]+array[j]+array[k] <= target:
                    result = max(result, array[i]+array[j]+array[k])
    
    return result

print("Result using BruteForceSolution: ",  bruteForceSolution([-2, 0, 1, 2], 2))
print("Result using BruteForceSolution: ",  bruteForceSolution([1, 0, 1, 1], 100))


'''
Solution 2: Optimized Approach

	If we sort the given array, we can take advantage of the two pointer approach to efficiently find a triplet

	we have first_pointer starting from 0 to array.length - 2 and

	a second_pointer and third_pointer starting from first_pointer + 1 and end of the array respectively.

	We need nearest value to target, which means it can less than or equal to target.
		we are considering a triplet if it is less than or equal to target
		we have used max() function to store the nearest value in result variable

	if first_pointer + sum_two_pointers equals is less than or equal to target
		store triplet in result
		
		increment the second_pointer: because we need to increase the two pointer sum
		

	if sum of first_pointer + sum_two_pointers is greater than target
	    decrement the third_pointer: because we need to decrease the two pointer sum


Time Complexity: O(n^2)

The outer loop iterates over each element of the array once, resulting in O(n) iterations.
Inside the outer loop, there's a two-pointer approach that iterates through the remaining elements of the array. 
This also results in O(n) iterations in the worst case.

'''

def mainSolution(array, target):

    result = float('-inf')

    for first_pointer in range(len(array)-2):
        
        second_pointer = first_pointer + 1
        third_pointer = len(array) - 1
        
        while second_pointer < third_pointer:
            two_pointer_sum = array[second_pointer] + array[third_pointer]
            
            if (array[first_pointer] + two_pointer_sum <= target):
                result = max(result, array[first_pointer] + two_pointer_sum)
                second_pointer += 1
            else:
                third_pointer -= 1
    
    return result

print("Result using mainSolution: ", mainSolution([-2, 0, 1, 2], 2))
print("Result using mainSolution: ", mainSolution([-3, -1, 1, 2], 1))
print("Result using mainSolution: ", mainSolution([1, 0, 1, 1], 100))
