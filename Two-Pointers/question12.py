'''
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
'''

def solution(array):
	print('array: ', array)
	#[1, 2, 5, 3, 7, 10, 9, 12]

	first_pointer = 0
	second_pointer = len(array) - 1
		
	minimum = float('inf')
	maximum = float('-inf')

	for first_pointer in range(1, len(array)):
		
		flag = False
		
		if array[first_pointer] < array[first_pointer-1]:
			flag = True
		
		if flag:
			minimum = min(minimum, array[first_pointer])


	for second_pointer in range(len(array)-2, -1, -1):
		flag = False
		
		if array[second_pointer] > array[second_pointer+1]:
			flag = True
		
		if flag:
			maximum = max(maximum, array[second_pointer])



	if first_pointer == len(array) - 1 and second_pointer == 0:
		return 0
	else:
		return (second_pointer-first_pointer) + 1


print('Result: ', solution([1, 2, 5, 3, 7, 10, 9, 12]))
print('Result: ', solution([1, 2, 3]))
print('Result: ', solution([3, 2, 1]))
