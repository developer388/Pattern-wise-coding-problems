'''
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, 
whose sum is equal to the target number.


Example 1:

	Input: [4, 1, 2, -1, 1, -3], target=1

	Output: [-3, -1, 1, 4], [-3, 1, 1, 2]

	Explanation: Both the quadruplets add up to the target.


Example 2:

	Input: [2, 0, -1, 1, -2, 2], target=2

	Output: [-2, 0, 2, 2], [-1, 0, 1, 2]

	Explanation: Both the quadruplets add up to the target.


https://leetcode.com/problems/4sum/

Similiar to Question no 5 (3sum problem)
'''


'''
Solution 1: Brute Force Approach

	In this approach we are using four nested loops, and if sum of a quardlet indicated by i, j, k, l equals target    
    
    we are first sorting the found quardlet and then checking it if it exists in our result array
        this way we will avoid duplicate quardlet in our result

Time Complexity: O(n^4)	
'''

def bruteForceSolution(arr, target):
	
	result = []
	
	for i in range(len(arr)-3):
	    for j in range(len(arr)-2):
	        for k in range(len(arr)-1):
	            for l in range(len(arr)):
	                
	                if arr[i] + arr[j] + arr[k] + arr[l] == target:
	                    
	                    quardlet = [arr[i], arr[j], arr[k], arr[l]]
	                    quardlet.sort()
	                    
	                    if quardlet not in result:
	                        result.append(quardlet)
	        
	return result
			

print("Result using bruteForceSolution: ", bruteForceSolution([4, 1, 2, -1, 1, -3], 1))



'''
Solution 2: Optimized Approach

    If we sort the given array, we can take advantage of two pointer approach to efficiently find a triplet

    we have first_pointer starting from 0 to array.length - 2 and

    a second_pointer and third_pointer starting from first_pointer + 1 and end of the array respectively.

    if first_pointer + sum_two_pointers equals zero we have found our triplet

    if sum of first_pointer + sum_two_pointers is less than zero 
        we have to increase the second_pointer to increase the sum

    if sum of first_pointer + sum_two_pointers is greater than zero 
        we have to decrease the third_pointer to decrease the sum

    to ensure we don't consider the duplicate triplets, in our result
    we need to put three checks as mentioned in code below


Time Complexity: O(n^3)

The outer loop iterates over each element of the array once, resulting in O(n) iterations.
Inside the outer loop, there's a two-pointer approach that iterates through the remaining elements of the array. 
This also results in O(n) iterations in the worst case.
'''

def mainSolution(array, target):

	array.sort()

	result = []

	print('array: ', array)

	for first_pointer in range(len(array)):

		if first_pointer > 0 and array[first_pointer] == array[first_pointer -1]:
			continue

		for second_pointer in range(first_pointer+1,  len(array)):

			if second_pointer != first_pointer+1 and array[second_pointer] == array[second_pointer -1]:
				continue

			third_pointer = second_pointer + 1
			fourth_pointer = len(array) - 1

			while third_pointer < fourth_pointer:

				four_pointer_sum = array[first_pointer] + array[second_pointer] + array[third_pointer] + array[fourth_pointer]

				if four_pointer_sum > target:
					fourth_pointer -= 1
				elif four_pointer_sum < target:
					third_pointer += 1
				else:
					result.append([array[first_pointer], array[second_pointer], array[third_pointer], array[fourth_pointer]])
					third_pointer += 1
					fourth_pointer -= 1

					while third_pointer<fourth_pointer and  array[third_pointer] == array[third_pointer-1]:
						third_pointer += 1

					while fourth_pointer < len(array)-2 and array[fourth_pointer] == array[fourth_pointer+1]:
						fourth_pointer -= 1

	return result


print("Result using mainSolution: ", mainSolution([4, 1, 2, -1, 1, -3], 1))
print("Result using mainSolution: ", mainSolution([2, 0, -1, 1, -2, 2], 2))
print("Result using mainSolution: ", mainSolution([2, 2, 2, 2, 2], 8))



# https://www.youtube.com/watch?v=eD95WRfh81c