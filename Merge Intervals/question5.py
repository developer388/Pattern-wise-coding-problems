'''
Given a list of intervals representing the start and end time of ‘N’ meetings, 
find the minimum number of rooms required to hold all the meetings.

Example 1:

	Meetings: [[1,4], [2,5], [7,9]]

	Output: 2

	Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. 
				 [7,9] can occur in any of the two rooms later.

Example 2:

	Meetings: [[6,7], [2,4], [8,12]]

	Output: 1

	Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

Example 3:

	Meetings: [[1,4], [2,3], [3,6]]

	Output:2

	Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], 
	we need two rooms to hold all the meetings.

Example 4:

	Meetings: [[4,5], [2,3], [2,4], [3,5]]
	
	Output: 2
	
	Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].


Leetcode URL: https://leetcode.com/problems/meeting-rooms-ii/

important
'''

'''
Solution 1: Optimized Approach

	We need to sort input array of intervals by start time so that we can 
	compare for the overlapping meetings in a loop

	we are using a min_heap, which stores the end time of the meeting

	to start with the we first insert the end time of first meeting in the min heap

	start a loop from 1 to N-1

	  if start_time of current meeting >= minimum end time so far (min_heap.peek()):
		
		  this means current meeting can be accommodated in an existing room. therefore,
		  we update the end time of the earliest meeting in the min-heap to be the 
		  end time of the current meeting. For this we do two operations
		   
		  min_heap.pop()
		  min_heap.push(end_time of current meeting)

	  If the current meeting cannot be accommodated in any existing room, allocate a new
	  room. Add the end time of the current meeting to the min-heap. For this we add a 
	  end time in min heap

	      min_heap.push(end_time of current meeting)


	 We require a min heap here because even if we sort the array, there can be cases where two 
	 non-consecutive meetings do not conflict (consider example 4). In such cases, to determine
	 whether a future meeting will conflict with the meetings we have processed so far, we need to 
	 compare the end time of the processed meeting that would have finished first. Therefore, a min
	 heap is necessary to retrieve the end time of the meeting that finished earlier.
'''

import heapq

def mainSolution(arr):
	
	arr.sort()
	
	min_heap = []
	
	heapq.heappush(min_heap, arr[0][1])
	
	for interval in range(1, len(arr)):
		
		if arr[interval][0] >= min_heap[0] :
			heapq.heappop(min_heap)
			heapq.heappush(min_heap, arr[interval][1])
		else:
			heapq.heappush(min_heap, arr[interval][1])
	return len(min_heap)
	
 
print("Result using mainSolution: ", mainSolution([[1,4], [2,5], [7,9]]))
print("Result using mainSolution: ", mainSolution([[6,7], [2,4], [8,12]]))
print("Result using mainSolution: ", mainSolution([[1,4], [2,3], [3,6]]))
print("Result using mainSolution: ", mainSolution([[4,5], [6,3], [2,4], [3,5]]))

