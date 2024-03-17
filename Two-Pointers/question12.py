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

Leetcode URL: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
'''



'''
Solution 1: Brute Force Solution

In this brute force solution, we iterate through all possible subarrays of the input array. 
For each subarray, we check if sorting it results in the entire array being sorted. 
If it does, we update the minimum length of the subarray. 

Finally, we return the smallest subarray length found. However, note that this solution has a 
time complexity of O(n^3), which is inefficient for larger input arrays.

'''

def bruteForceSolution(arr):
    min_length = len(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            subarray = arr[i:j]
            if sorted(subarray) == subarray:
                min_length = min(min_length, j - i)
    return min_length




'''
Solution 1: Optimized Approach

	Use two pointer: first_pointer starting from begining and 
	second_pointer starting from the end
	
	for first_pointer if arr[first_pointer] <= arr[first_pointer + 1]:
		ascending sorting order is maintained therefore increment the first_pointer

	for second_pointer if arr[second_pointer] >= arr[second_pointer - 1]:
		descending sorting order is maintained therefore decrement the second_pointer

	to handle cases like example no. 2:
		we need to find minimum and maximum value of the subarray

	by comparing miniumum and maximum value of the subarray
	    we adjust our first_pointer and second_pointer to consider the values that are 
	    related to various edge cases and are out of order


Time Complexity is O(n)

as we are running n iterations + some subarray iterations

'''

def mainSolution(arr):

	if len(arr) <= 1:
		return 0

	first_pointer = 0
	second_pointer = len(arr) - 1

	# Find the first index from the left where the order breaks
	while first_pointer < len(arr) - 1 and arr[first_pointer] <= arr[first_pointer + 1]:
		first_pointer += 1

	# The array is already sorted
	if first_pointer == len(arr) - 1:
		return 0

	# Find the first index from the right where the order breaks
	while second_pointer > 0 and arr[second_pointer] >= arr[second_pointer - 1]:
		second_pointer -= 1

	# Find the minimum and maximum values within the unsorted subarray
	minimum_value_in_subarray = float('inf')
	maximum_value_in_subarray = float('-inf')
	
	for subarray_index in range(first_pointer, second_pointer + 1):
		minimum_value_in_subarray = min(minimum_value_in_subarray, arr[subarray_index])
		maximum_value_in_subarray = max(maximum_value_in_subarray, arr[subarray_index])


	# Extend the subarray to include elements that are out of order
	while first_pointer > 0 and arr[first_pointer - 1] > minimum_value_in_subarray:
		first_pointer -= 1
	
	while second_pointer < len(arr) - 1 and arr[second_pointer + 1] < maximum_value_in_subarray:
		second_pointer += 1

	return second_pointer - first_pointer + 1


print("Result using MainSolution: ", mainSolution([1, 2, 5, 3, 7, 10, 9, 12]))
print("Result using MainSolution: ", mainSolution([1, 2, 3]))
print("Result using MainSolution: ", mainSolution([3, 2, 1]))
