'''
Given a sorted array, create a new array containing squares of all the number 
of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]



approach:
	
	set second_pointer to first positive value in array
	set first_pointer to first negative value in array
	
	
	first pointer will be decremented to move towards beggining of array
	second pointer will incremented to move towards end of the array


	calculate square of no. of both the pointers and compare them 

'''

def solution(array):

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

print('Result: ', solution([-2, -1, 0, 2, 3]))
print('Result: ', solution([ -2 ,-1, 0, 3, 4, 5]))
print('Result: ', solution([ 0, 3, 4, 5]))