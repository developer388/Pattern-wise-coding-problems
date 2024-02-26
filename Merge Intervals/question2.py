'''

Given a list of non-overlapping intervals sorted by their start time,
insert a given interval at the correct position and merge all necessary 
intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
 

Observation:
	
	input is sorted by start_time


'''


def solution(array, new_interval):

	start_time = array[0][0]
	end_time = array[0][1]

	result = []

	i = 0

	print('insert non conflicting:')
	while  i < len(array) and array[i][1] < new_interval[0]: 
		result.append([array[i][0], array[i][1]])
		i += 1
	
	print(result)

	print('insert merged: ')

	while i < len(array) and array[i][0] <= new_interval[1]:
		new_interval[0] = min(new_interval[0], array[i][0])
		new_interval[1] = max(new_interval[1], array[i][1])
		i += 1

	result.append([new_interval[0], new_interval[1]])

	print(result, i)

	print('insert remaining:')
	while i < len(array):
		result.append([array[i][0], array[i][1]])
		i += 1

	print(result)
	return result

print('Result: ', solution([[1,3], [4,7], [8,12]], [4,6]))
print('Result: ', solution([[1,3], [5,7], [8,12]], [4,10]))