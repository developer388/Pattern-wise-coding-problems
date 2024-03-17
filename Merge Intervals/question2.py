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
 
Leetcode URL: https://leetcode.com/problems/insert-interval/
'''


'''
Solution 1: Optimized Approach

	initialize a index variable as 0

	while :
		there is no conflict, insert the ith interval to result
		increment the index

	while:
		there is a conflict: stretch new_interval using min, max
		incremment the index

	add new_interval to the result

	while:
		add the interval
		increment the index

'''


def mainSolution(array, new_interval):

	if len(array) == 0 :
			return [new_interval]
		
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

print("Result using mainSolution: ", mainSolution([[1,3], [4,7], [8,12]], [4,6]))
print("Result using mainSolution: ", mainSolution([[1,3], [5,7], [8,12]], [4,10]))



'''
Solution 2: Optimized Approach

	Initialize an empty list to store the merged intervals.

	Iterate through the sorted intervals:

		If the current interval ends before the new interval starts, or if the current interval starts 
		after the new interval ends, add the current interval to the result list.

		If there's an overlap between the current interval and the new interval, merge them:

			Update the start time of the new interval to be the minimum of the current interval's start time and the new interval's start time.

			Update the end time of the new interval to be the maximum of the current interval's end time and the new interval's end time.

	Add the new interval to the result list.

	Return the result list.

'''


def solution2(array, new_interval):
    result = []
    inserted = False

    for interval in array:
        if interval[1] < new_interval[0]:  # No overlap, interval ends before new interval starts
            result.append(interval)
        elif interval[0] > new_interval[1]:  # No overlap, interval starts after new interval ends
            if not inserted:
                result.append(new_interval)
                inserted = True
            result.append(interval)
        else:  # Overlap, merge intervals
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])

    if not inserted:
        result.append(new_interval)

    return result