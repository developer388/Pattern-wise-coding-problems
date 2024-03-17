'''
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually
 exclusive intervals.

Example 1:

	Intervals: [[1,4], [2,5], [7,9]]
	
	Output: [[1,5], [7,9]]
	
	Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

Example 2:

	Intervals: [[6,7], [2,4], [5,9]]

	Output: [[2,4], [5,9]]

	Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example: 3

	Intervals: [[1,4], [2,6], [3,5]]

	Output: [[1,6]]

	Explanation: Since all the given intervals overlap, we merged them into one.


Leetcode URL: https://leetcode.com/problems/merge-intervals/

Approach:
	1. sort the input intervals based on start time
	2. store start and end of first interval in start, end variable
	3. start the loop from 1st index
	4. compare start interval of ith iteration with end interval of previous interval
	5. if start interval of ith interation is less than end interval of previous interval
		   extend the end interval of previous interval to max of both the intervals
    6. push the interval to result array
    	set start and end to ith interval

'''


def solution(array):

	array.sort()

	print(array)

	start = array[0][0]
	end = array[0][1]

	result = []

	for i in range(1, len(array)):


		# if start of interval is less than end of last interval
		# then merge intervals

	    if array[i][0] <= end:
	    	end = max(array[i][1], end)
	    else:
	    	result.append([start, end])	
	    	start = array[i][0]
	    	end = array[i][1]


	   
	result.append([start, end])
	return result
		



#print("Result: ", solution([[1,4], [2,5], [7,9]])) 


print("Result: ", solution([[1,4], [2,6], [3,5]]	)) 

'''
Solution 2: Optimized Approach

	Sort the intervals:

		Start by sorting the input array of intervals based on their start time. This step ensures that overlapping 
		intervals are adjacent to each other, making it easier to identify and merge them.
	
	Initialize an empty list for the result:

		Create an empty list to store the merged intervals.
	
	Iterate through the sorted intervals:

		Loop through each interval in the sorted array, except for the last one.
	
	Check for overlap:

		For each interval, compare its end time with the start time of the next interval. If there's an overlap (i.e., if the end time of the current interval is greater than or equal to the start time of the next interval), proceed to merge them.
	
	Merge overlapping intervals:

		Update the start time of the next interval to be the minimum of the current interval's start time and the next interval's start time.
		Update the end time of the next interval to be the maximum of the current interval's end time and the next interval's end time.

	Append non-overlapping intervals to the result:

		If there's no overlap between the current interval and the next one, append the current interval to the result list.
		Append the last interval:

		After the loop, append the last interval to the result list.
		Return the result:

	Finally, return the list containing the merged intervals.

'''

def solution2(array):
	array.sort()
	result = []
	
	for interval in range(len(array) - 1):
		next_interval = interval + 1
		
		# Check for overlap
		if array[interval][1] >= array[next_interval][0]:
			array[next_interval][0] = min(array[interval][0], array[next_interval][0])
			array[next_interval][1] = max(array[interval][1], array[next_interval][1])
		else:
			result.append(array[interval])

	# Append the last interval
	result.append(array[-1])
	
	return result

