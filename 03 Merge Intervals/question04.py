'''
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

	Appointments: [[1,4], [2,5], [7,9]]
	
	Output: false
	
	Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:

	Appointments: [[6,7], [2,4], [8,12]]

	Output: true

	Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:

	Appointments: [[4,5], [2,3], [3,6]]
				  [[2,3], [3,6], [4,5]]

	Output: false

	Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

'''

'''
Solution 1: Optimized Approach
		
		sort the input intervals

		start a loop from 0 to N-1:
			next_interval = interval + 1

			if current interval and next interval overlaps: 
            	return False
		
		return False
'''


def mainSolution(arr):

    arr.sort()

    for interval in range(len(arr)-1):
        next_interval = interval + 1
        
        if arr[interval][1] > arr[next_interval][0]:
            return False
    
    return True
    
    
    
print("Result using mainSolution: ", mainSolution([[1,4], [2,5], [7,9]]))
print("Result using mainSolution: ", mainSolution([[6,7], [2,4], [8,12]]))
print("Result using mainSolution: ", mainSolution([[4,5], [2,3], [3,6]]))





'''
Solution 2: Optimized Approach
		
		sort the input intervals

		start a loop from 0 to N-1:
			next_interval = interval + 1

			if current interval and next interval overlaps: 
            	return False
		
		return False
'''

def solution2(array):

	array.sort()

	start_time = array[0][0]
	end_time = array[0][1]

	for i in range(1, len(array)):

		if array[i][0] < end_time:
			return False

		start_time = array[i][0]
		end_time = array[i][1]

	return True

print('Result using solution2: ', solution2([[1,4], [2,5], [7,9]]))
print('Result using solution2: ', solution2([[6,7], [2,4], [8,12]]))
print('Result using solution2: ', solution2([[4,5], [2,3], [3,6]]))