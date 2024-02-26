'''
Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

The constructor of the class should accept an integer array containing initial numbers 
from the stream and an integer ‘K’.

The class should expose a function add(int num) which will store the given number and
return the Kth largest number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 4
	   [1, 2, 3, 5, 6, 11, 12]

1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
'''

import heapq

class Stream:

	def __init__(self, array, k):
		self.min_heap = []

		for index in range(len(array)):
			heapq.heappush(self.min_heap, array[index])

			if index > (k-1):
				heapq.heappop(self.min_heap)

	def add(self, number):
		heapq.heappush(self.min_heap, number)
		heapq.heappop(self.min_heap)

		# print(self.min_heap)
		return self.min_heap[0]



stream = Stream([3, 1, 5, 12, 2, 11], 4)
print('Result: ', stream.add(6))
print('Result: ', stream.add(13))
print('Result: ', stream.add(4))

#print(stream.array)



