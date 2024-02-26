'''
Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5). The Euclidean distance between (1, 3) and the origin is sqrt(10). Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
'''
import heapq

def solution(points, k):

	max_heap = []

	for index in range(len(points)):
		
		distance =  (points[index][0]**2) + (points[index][1]**2)
			
		if index < k:
			heapq.heappush(max_heap, (-distance, index))			
		else:
			if -distance > max_heap[0][0]:
				heapq.heappop(max_heap)
				heapq.heappush(max_heap, (-distance, index))


	return max_heap


print('Result: ', solution([[1,2],[1,3]], 1)) 

print('Result: ', solution([[1, 3], [3, 4], [2, -1]], 2))