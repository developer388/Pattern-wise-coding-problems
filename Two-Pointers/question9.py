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

[2, 2, 0, 1, 2, 0]
[0, 2, 0, 1, 2, 2]
[0, 1, 0, 2, 2, 2]

Output: [0 0 1 2 2 2 ]



Approach:

	use three pointer

	
'''


def solution(array):
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




#print('Result: ', solution([1, 0, 2, 1, 0]))


print('Result: ', solution([2, 2, 0, 1, 2, 0]))

