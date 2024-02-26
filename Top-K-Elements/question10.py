'''
Given an array, find the sum of all numbers 
between the K1’th and K2’th smallest elements of that array.

Example 1:

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15.
 The sum of numbers coming between 5 and 15 is 23 (11+12).

Example 2:

Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12
Explanation: The sum of the numbers between the 1st smallest number (3) 
and the 4th smallest number (8) is 12 (5+7).

[1, 3, 12, 5, 15, 11]

1, 3, 5, 11, 12, 15

'''




import heapq

def solution(array, k1, k2):

	max_heap = []

	for index in range(len(array)):

		heapq.heappush(max_heap, -array[index])

		if index > (k2-1):
			heapq.heappop(max_heap)

	
	result = 0

	d = (k2-k1)+1


	for i in range(d):
		number = (-heapq.heappop(max_heap))
		if i>0 and i<(d-1):
			result += number

	return result

print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))


print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))
print('Result: ', solution([1, 3, 12, 5, 15, 11], 3, 6))

print('Result: ', solution([3, 5, 8, 7], 1, 4))