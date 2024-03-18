'''
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, 
not the Kth distinct element.

Note: For a detailed discussion about different approaches to solve this problem, 
take a look at Kth Smallest Number.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are
 [1, 2].

Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are
 [1, 2, 5].

Example 3:

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are 
[5, -1].
'''

import heapq

def solution(array, k):

	max_heap = []

	for index in range(k):

		heapq.heappush(max_heap, -array[index])

	for index in range(k, len(array)):

		if -array[index] > max_heap[0]:
			heapq.heappop(max_heap)
			heapq.heappush(max_heap,-array[index])


	print(max_heap)

	return -max_heap[0]


def solution2(array, k):
	max_heap = []

	for index in range(len(array)):

		if index < k:
			heapq.heappush(max_heap, -array[index])
		else:
			if -array[index] > max_heap[0]:
				heapq.heappop(max_heap)
				heapq.heappush(max_heap,-array[index])


	print('1st: ', -heapq.heappop(max_heap))

	print('2nd: ', -heapq.heappop(max_heap))

	print('3rd: ', -heapq.heappop(max_heap))
	return max_heap

# print('Result: ', solution([1, 5, 12, 2, 11, 5], 3))

# print('Result: ', solution([1, 5, 12, 2, 11, 5], 4))

# print('Result: ', solution([5, 12, 11, -1, 12], 3))

a = [20,1,4,56,12,3,7]
a.sort()
print(a)
print('Result: ', solution2([20,1,4,56,12,3,7], 3))
