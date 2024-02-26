'''

Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically 
increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any 
index i in the array arr[i] != arr[i+1].

Example 1:

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

Example 2:

Input: [3, 8, 3, 1]
Output: 8
Example 3:

Input: [1, 3, 8, 12]
Output: 12
Example 4:

Input: [10, 9, 8]
Output: 10

'''

def solution(array):

	start = 0
	end = len(array) - 1

	while start <= end:

		mid = (start + end) // 2

		if mid+1 > len(array)-1:
			return array[start]
			
		if array[mid] <= array[mid+1]:
			start = mid + 1
		else:
			end = mid - 1
		
	return array[start]





print('Result: ', solution([1, 3, 8, 12, 4, 2]))
print('Result: ', solution([3, 8, 3, 1]))
print('Result: ', solution([1, 3, 8, 12]))
print('Result: ', solution([10, 9, 8]))
