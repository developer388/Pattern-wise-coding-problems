'''
Given a sorted array, create a new array containing squares of all the number 
of the input array in the sorted order.

Example 1:

	Input: [-2, -1, 0, 2, 3]

	Output: [0, 1, 4, 4, 9]

Example 2:

	Input: [-3, -1, 0, 1, 2]

	Output: [0 1 1 4 9]


Leetcode URL: https://leetcode.com/problems/squares-of-a-sorted-array/
'''

'''
Solution 2: Optimized Approach 1
	
	In this approach, we set first_pointer and second_pointer to start and end of the array.

	Because input array is sorted and it contains positive and negative values, 
	if set our first_pointer to 0th index and second_pointer to the last index of the input array, we will get one of the 
	value which will have largest square, 
	
	we can initialize an array of length equivalent to equal to input array
	we can start filling our result array from the end (len(arr)-1). (As input array is sorted, our result array will also be sorted)
	
	A result_index can be used to insert the value value in result array starting from the end till 0th index.

	we can compare the abs values of first_pointer and second_pointer, and add the square to the result_pointer index in result array
'''


def mainSolution(arr):
    first_pointer = 0
    second_pointer = len(arr) - 1
    
    result = [None] * len(arr)
    result_index = len(arr) - 1
    
    while first_pointer <= second_pointer:
        
        if abs(arr[second_pointer] >= abs(arr[first_pointer])):
            result[result_index] = pow(arr[second_pointer], 2)
            second_pointer -= 1
            result_index -= 1
            
        else:
            result[result_index] = pow(arr[first_pointer], 2)
            first_pointer += 1
            result_index -= 1
            
    
    return result



print("Result using mainSolution: ", mainSolution([-2, -1, 0, 2, 3]))
print("Result using mainSolution: ", mainSolution([ -2 ,-1, 0, 3, 4, 5]))
print("Result using mainSolution: ", mainSolution([ 0, 3, 4, 5]))



'''
Solution 2: Optimized Approach 2

	Because input array is sorted, if set our first_pointer and second_pointer to middle of the array,
	we can compare the left square and right square to insert square values in result array starting from 0th index
	

	To set and find the middle of the array, we can set our second_pointer to first positive value in input array,
	the first negative value will be an immediate neighbour and can be then found at second_pointer -1
	
	once we have set,
	   second_pointer to first positive value in the array
	   first_pointer to first negative value in the array
	
	
	first pointer will be decremented to move towards beggining of array
	second pointer will incremented to move towards end of the array
	
'''

def solution2(array):

	first_pointer = 0
	second_pointer = 0

	for i in range(len(array)):
		if array[i]>=0:
			second_pointer = i
			break

	first_pointer = second_pointer - 1


	result = []


	while second_pointer<len(array) :

		print(first_pointer, second_pointer)
		
		right_square = array[second_pointer] * array[second_pointer]

		if first_pointer >= 0:

			left_square = array[first_pointer] * array[first_pointer]
			
			if (left_square <= right_square):
				result.append(left_square)
				first_pointer -= 1
			else:
				result.append(right_square)
				second_pointer += 1

		else:
			result.append(right_square)
			second_pointer += 1


	return result


print("Result using solution2: ", solution2([-2, -1, 0, 2, 3]))
print("Result using solution2: ", solution2([ -2 ,-1, 0, 3, 4, 5]))
print("Result using solution2: ", solution2([ 0, 3, 4, 5]))
