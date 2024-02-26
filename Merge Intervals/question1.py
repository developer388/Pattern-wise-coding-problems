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

	    if array[i][0] < end:
	    	end = max(array[i][1], end)
	    else:
	    	result.append([start, end])	
	    	start = array[i][0]
	    	end = array[i][1]


	   
	result.append([start, end])
	return result
		



#print("Result: ", solution([[1,4], [2,5], [7,9]])) 


print("Result: ", solution([[1,4], [2,6], [3,5]]	)) 


