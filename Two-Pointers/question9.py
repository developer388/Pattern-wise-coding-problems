'''

Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array. 
The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers that is why it is called Dutch National Flag 
problem.

Example 1:
	
	Input: [1, 0, 2, 1, 0]
	
	Output: [0 0 1 1 2]

Example 2:

	Input: [2, 2, 0, 1, 2, 0]

	Output: [0 0 1 2 2 2 ]

'''


'''

Solution 1: Optimized Approach 1

	we can use three pointers

	first_pointer will start from 0th index  : used to represent 0s
	second_pointer will start from 0th index : used to represent 1s
	third pointer will start from the end the array : used to represent 2s

	because we only three unique value in given array,
	we can compare our second_pointer with the value and swap with another pointer

	if second_pointer has 0:
		 swap(second and first)
		 increment both first and second pointers

	else if second_pointer has 1
	     no swap required
		 increment second pointer
	
	else if second_pointer has 2
		 swap(second and third)
		 decrement third_pointer

	
	A important observation here:
	Because we are using three pointers, we could have started the second_pointer from index 1
	but if do so and and because we are only checking second_pointer against ith value, we will
	miss the value stored in 0th index, if we start from the 1st index.

	that's why we have started both first and second pointer from 0th index, by this we may swap even
	if it is not required but we will never miss a value in our consideration

'''


def mainSolution(array):
	first_pointer = 0
	second_pointer = 0
	third_pointer = len(array) - 1


	while second_pointer <= third_pointer:

		if array[second_pointer] == 0:
			array[second_pointer], array[first_pointer] = array[first_pointer], array[second_pointer]
			
			first_pointer += 1
			second_pointer += 1

		
		elif array[second_pointer] == 1:
			second_pointer+= 1

		elif array[second_pointer] == 2:
			array[third_pointer], array[second_pointer] = array[second_pointer], array[third_pointer]
			third_pointer -= 1
			
	return array


print("Result using mainSolution: ", solution([2, 2, 0, 1, 2, 0]))

