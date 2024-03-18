'''
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.

Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.

'''

import heapq

def solution(array, k):

	frequency_map = {}

	for num in array:
		if num not in frequency_map:
			frequency_map[num] = 1
		else:
			frequency_map[num] += 1

	min_heap = []

	for key in frequency_map:
		heapq.heappush(min_heap, (frequency_map[key], key))

		if len(min_heap) > k:
			heapq.heappop(min_heap)

	result = []
	while min_heap:
		result.append(heapq.heappop(min_heap)[1])
	return result




print('Result: ', solution([1, 3,3,3 ,5, 12, 11, 12,11, 11], 2))
print('Result: ', solution([5, 12, 11, 3, 11], 2))
