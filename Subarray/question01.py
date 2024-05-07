# Write a function that returns all subarrays of a given array.


# Iterative Method
def solution1(array):

	result = []

	for first_pointer in range(0, len(array)):

		
		for second_pointer in range(first_pointer, len(array)):

			subarray = []

			for index in range(first_pointer, second_pointer+1):
				subarray.append(array[index])
		

			result.append(subarray)


	return result

print("Result using iterative method: ", solution1([1, 2, 3]))


# Recursive Method
def solution2(array, result, first_pointer, second_pointer):

	if second_pointer == len(array):
		return result

	elif first_pointer > second_pointer:
		return solution2(array, result, 0, second_pointer+1)
	else:

		sub_array = []
		
		for i in range(first_pointer, second_pointer+1):
			sub_array.append(array[i])
		
		result.append(sub_array)
		
		solution2(array, result, first_pointer+1, second_pointer)
		
	return result
	

print('Result using recursive method: ', solution2([1, 2, 3], [],  0, 0))