'''
Given a sorted number array and two integers ‘K’ and ‘X’,
find ‘K’ closest numbers to ‘X’ in the array. 
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
'''

import heapq

def solution(array, k, x):

	min_heap = []

	for index in range(len(array)):
		heapq.heappush(min_heap, (( - abs(x - array[index]), index) ))

		if index > (k-1):
			heapq.heappop(min_heap)

	result = []

	while min_heap:
		result.append(array[heapq.heappop(min_heap)[1]])

	return result





print('Result: ', solution([5, 6, 7, 8, 9], 3, 7))

print('Result: ', solution([2, 4, 5, 6, 9], 3, 6))

print('Result: ', solution([2, 4, 5, 6, 9], 3, 10))