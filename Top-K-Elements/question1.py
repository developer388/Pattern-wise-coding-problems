'''
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, 
take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]

'''

import heapq

def solution(array, k):

	min_heap = []

	for index in range(k):
		heapq.heappush(min_heap, array[index])

	for index in range(k, len(array)):

		if array[index] > min_heap[0]:
			heapq.heappop(min_heap)
			heapq.heappush(min_heap, array[index])

	return list(min_heap)

def solution2(array, k):

	min_heap = []

	for index in range(len(array)):
		heapq.heappush(min_heap, array[index])

		if index > k-1:
			heapq.heappop(min_heap)
			
		# if index < k:			
		# 	heapq.heappush(min_heap, array[index])
		# else:
		# 	if array[index] > min_heap[0]:
		# 		heapq.heappop(min_heap)
		# 		heapq.heappush(min_heap, array[index])

	print('1st: ', heapq.heappop(min_heap))

	print('2nd: ', heapq.heappop(min_heap))

	print('3rd: ', heapq.heappop(min_heap))
	return list(min_heap)
# print('Result: ', solution([3, 1, 5, 12, 2, 11], 3))
# print('Result: ', solution([5, 12, 11, -1, 12], 3))

a = [20,1,4,56,12,3,7]
a.sort()
print(a)
print('Result: ', solution2([20,1,4,56,12,3,7], 3))


#print('Result: ', solution([5, 12, 11, -1, 12], 3))
